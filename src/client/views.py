from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Subscription, PlanChoice
from writer.models import Article
from common.django_utils import arender
from common.auth import aclient_required # type: ignore
from common.auth import aget_user



@aclient_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    subscription_plan = 'No subscription yet'
    if subscription := await Subscription.afor_user(user):
        subscription_plan = 'premium' if await subscription.ais_premium() else 'standard'
        if not subscription.is_active:
            subscription_plan += ' (inactive)'
    try:
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        has_subscription = True
        subscription_name = (await subscription.aplan_choice()).name
    except ObjectDoesNotExist:
        has_subscription = False
        subscription_name = 'No subscription yet'

    context = {
        'has_subscription': has_subscription,
        'subscription_plan': subscription_plan,
        'subscription_name': subscription_name
    }
    return await arender(request, 'client/dashboard.html', context)

@aclient_required
async def browse_articles(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    try:
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        has_subscription = True
        subscription_plan = 'premium' if await subscription.ais_premium() else 'standard'
        if not await subscription.ais_premium():
            articles = Article.objects.filter(is_premium = False).select_related('user')
        else:
            articles = Article.objects.all().select_related('user')
    except ObjectDoesNotExist:
        has_subscription = False
        subscription_plan = 'none'
        articles = []

    context = {
        'has_subscription': has_subscription, 
        'articles': articles,
        'subscription_plan': subscription_plan,
    }
    return await arender(request, 'client/browse-articles.html', context)

@aclient_required
async def subscribe_plan(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    if await Subscription.afor_user(user):
        return redirect('client-dashboard')
    context = {'plan_choices': PlanChoice.objects.filter(is_active = True)}
    return await arender(request, 'client/subscribe-plan.html', context)

@aclient_required
async def update_user(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    try:
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        has_subscription = True
        subscription_plan = 'premium' if await subscription.ais_premium() else 'standard'
        subscription_name = (await subscription.aplan_choice()).name
    except ObjectDoesNotExist:
        has_subscription = False
        subscription_plan = 'none'
        subscription_name = 'No subscription yet'

    context = {
        'has_subscription': bool(await Subscription.afor_user(user)),
        'subscription_plan': subscription_plan,
        'subscription_name': subscription_name
    }
    return await arender(request, 'client/update-user.html', context)

@aclient_required
async def create_subscription(
    request: HttpRequest,
    sub_id: str,
    plan_code: str,
) -> HttpResponse:
    user = await aget_user(request)

    if await Subscription.afor_user(user):
        return redirect('client-dashboard')

    plan_choice = await PlanChoice.afrom_plan_code(plan_code)
    await Subscription.objects.acreate(
        plan_choice = plan_choice,
        cost = plan_choice.cost,
        external_subscription_id = sub_id,
        is_active = True,
        user = user,
    )

    context = {'subscription_plan': plan_choice.name}
    return await arender(request, 'client/create-subscription.html', context)