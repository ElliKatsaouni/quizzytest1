from django.shortcuts import render

from quizzy.filters import WeekdayFilter
from quizzy.forms import UserProfileForm, PubForm, QuizForm
from quizzy.models import City, Pub, Quiz, User, UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import django_filters


def index(request):
    city_list = City.objects.order_by('name')
    context_dict = {'cities': city_list}
    print(city_list)
    print(len(city_list))

    return render(request, 'quizzy/index.html', context_dict)


def about(request):
    return render(request, 'quizzy/about.html')


def home(request, city_name_slug):
    context_dict = {}
    try:
        city = City.objects.get(slug=city_name_slug)
        pubs = Pub.objects.filter(city=city)
        pub_ids = []
        for pub in pubs:
            pub_ids.append(pub.id)
        quizzes = Quiz.objects.filter(pub__in=pub_ids)
        quiz_filter = WeekdayFilter(request.GET, queryset=quizzes)

        context_dict['city'] = city
        context_dict['pubs'] = pubs
        context_dict['quizzes'] = quizzes
        context_dict['filter'] = quiz_filter

    except City.DoesNotExist:
        context_dict['city'] = None
        context_dict['pubs'] = None
        context_dict['quizzes'] = None

    return render(request, 'quizzy/home.html', context_dict)


def show_pub(request, city_name_slug, pub_name_slug,):
    context_dict = {}

    try:
        city = City.objects.get(slug=city_name_slug)
        pub = Pub.objects.get(slug=pub_name_slug)
        quizzes = Quiz.objects.filter(pub=pub)

        context_dict['pubid'] = pub.id
        context_dict['city'] = city
        context_dict['pub'] = pub
        context_dict['quizzes'] = quizzes
        context_dict['picture'] = pub.picture

    except City.DoesNotExist:
        context_dict['city'] = None
        context_dict['pub'] = None
        context_dict['quizzes'] = None
        context_dict['picture'] = None

    return render(request, 'quizzy/pub.html', context_dict)


@login_required
def add_pub(request, city_name_slug):
    try:
        city = City.objects.get(slug=city_name_slug)
    except City.DoesNotExist:
        city = None

    form = PubForm()
    if request.method == 'POST':
        form = PubForm(request.POST, request.FILES)
        if form.is_valid():
            if city:
                pub = form.save(commit=False)
                pub.city = city
                pub.slug = pub.name
                pub.save()
                return HttpResponseRedirect(reverse('add_quiz', kwargs={'city_name_slug': city_name_slug,
                                                                        'pub_name_slug': pub.slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'city': city}

    return render(request, 'quizzy/add_pub.html', context_dict)


@login_required
def add_quiz(request, city_name_slug, pub_name_slug):
    try:
        city = City.objects.get(slug=city_name_slug)
        pub = Pub.objects.get(slug=pub_name_slug)
    except City.DoesNotExist:
        city = None
        pub = None

    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            if pub:
                quiz = form.save(commit=False)
                quiz.pub = pub
                quiz.save()
                return HttpResponseRedirect(reverse('show_pub', kwargs={'city_name_slug': city_name_slug,
                                                                        'pub_name_slug': pub_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'pub': pub, 'city': city}

    return render(request, 'quizzy/add_quiz.html', context_dict)


@login_required
def update_pub(request, city_name_slug, pub_name_slug):

    try:
        city = City.objects.get(slug=city_name_slug)
        pub = Pub.objects.get(slug=pub_name_slug)

        if request.method == 'GET':
            form = PubForm(instance=pub)
            context_dict = {'form': form, 'pub': pub, 'city': city}

            return render(request, 'quizzy/update_pub.html', context_dict)

        elif request.method == 'POST':
            form = PubForm(request.POST, request.FILES, instance=pub)
            if form.is_valid():
                if city:
                    pub = form.save(commit=False)
                    pub.city = city
                    pub.save()
                    return HttpResponseRedirect(reverse('show_pub', kwargs={'city_name_slug': city_name_slug,
                                                                            'pub_name_slug': pub_name_slug}))

    except Pub.DoesNotExist:
        print("pub doesnt exist, do something")
        city = None
        pub = None

    return HttpResponse("NOOOOO")


@login_required
def update_quiz(request, city_name_slug, pub_name_slug, quiz_id):

    try:
        city = City.objects.get(slug=city_name_slug)
        pub = Pub.objects.get(slug=pub_name_slug)
        quiz = Quiz.objects.get(id=int(quiz_id))

        if request.method == 'GET':
            if quiz_id:
                form = QuizForm(instance=quiz)
                context_dict = {'form': form, 'pub': pub, 'city': city, 'quiz': quiz, 'quiz_id': quiz_id}
                return render(request, 'quizzy/update_quiz.html', context_dict)

        elif request.method == 'POST':
            form = QuizForm(request.POST, instance=quiz)
            if form.is_valid():
                if pub:
                    quiz = form.save(commit=False)
                    quiz.pub = pub
                    quiz.save()
                    return HttpResponseRedirect(reverse('show_pub', kwargs={'city_name_slug': city_name_slug,
                                                                            'pub_name_slug': pub_name_slug}))

    except Quiz.DoesNotExist:
        print("pub doesnt exist, do something")
        city = None
        pub = None
        quiz = None

    return HttpResponse("Ups...something went wrong")


def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('registration_complete')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'quizzy/profile_registration.html', context_dict)


@login_required
def password_change_done(request):
    return render(request, 'registration/password_change_done.html', )


@login_required
def profile(request):
    try:
        # user = User.objects.get(username=username)
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    return render(request, 'quizzy/profile.html',
        {'userprofile': userprofile, 'selecteduser': user, 'form': form})


@login_required
def like_quiz(request):
    quiz_id = None
    user_id = None
    if request.method == 'GET':
        quiz_id = request.GET['quiz_id']
        user_id = request.GET['user_id']
    upvotes = 0
    if quiz_id and user_id:
        quiz = Quiz.objects.get(id=int(quiz_id))
        user = User.objects.get(id=int(user_id))
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        if quiz:
            upvotes = quiz.upVotes + 1
            quiz.upVotes = upvotes
            quiz.save()
        if userprofile:
            userprofile.ratedquizzes.add(quiz)
            userprofile.save()
    return HttpResponse(upvotes)


@login_required
def dislike_quiz(request):
    quiz_id = None
    user_id = None
    if request.method == 'GET':
        quiz_id = request.GET['quiz_id']
        user_id = request.GET['user_id']
    downvotes = 0
    if quiz_id and user_id:
        quiz = Quiz.objects.get(id=int(quiz_id))
        user = User.objects.get(id=int(user_id))
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        if quiz:
            downvotes = quiz.downVotes + 1
            quiz.downVotes = downvotes
            quiz.save()
        if userprofile:
            userprofile.ratedquizzes.add(quiz)
            userprofile.save()
    return HttpResponse(downvotes)


def get_pub_list(max_results=0, starts_with=''):
    pub_list = []
    if starts_with:
        pub_list = Pub.objects.filter(name__istartswith=starts_with)

        if max_results > 0:
            if len(pub_list) > max_results:
                pub_list = pub_list[:max_results]
    return pub_list


def suggest_pub(request):
    pub_list = []
    starts_with = ''

    if request.method == 'GET' and 'suggestion' in request.GET:
        starts_with = request.GET['suggestion']
    pub_list = get_pub_list(8, starts_with)

    return render(request, 'quizzy/suggestions.html', {'pubs': pub_list})


@login_required #also unfavorites it!
def favorite_quiz(request):
    quiz_id = None
    user_id = None
    if request.method == 'GET':
        quiz_id = request.GET['quiz_id']
        user_id = request.GET['user_id']

    if quiz_id and user_id:
        quiz = Quiz.objects.get(id=int(quiz_id))
        user = User.objects.get(id=int(user_id))
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        if quiz and userprofile:
            if quiz in userprofile.favorites.all():
                userprofile.favorites.remove(quiz)
            else:
                userprofile.favorites.add(quiz)
                userprofile.save()
    return HttpResponse("success")

