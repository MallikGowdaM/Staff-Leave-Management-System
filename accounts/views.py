from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from accounts.models import profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from leave.models import Leave


def _pending_badge():
    """Returns count of pending leaves for the notification badge."""
    return Leave.objects.filter(status='Pending').count()


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role     = request.POST['role']
        user     = User.objects.create_user(username=username, password=password)
        profile.objects.create(user=user, role=role)
        return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('staff_dashboard')
        return render(request, 'login.html', {'error': True})
    return render(request, 'login.html')


@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    pending  = Leave.objects.filter(status='Pending').count()
    approved = Leave.objects.filter(status='Approved').count()
    rejected = Leave.objects.filter(status='Rejected').count()
    total    = pending + approved + rejected
    return render(request, 'admin_dashboard.html', {
        'total_leaves':    total,
        'pending_leaves':  pending,
        'approved_leaves': approved,
        'rejected_leaves': rejected,
        'pending_badge':   pending,       # sidebar notification badge
    })


@login_required
def staff_dashboard(request):
    my_leaves = Leave.objects.filter(user=request.user)
    return render(request, 'staff_dashboard.html', {
        'total_my':    my_leaves.count(),
        'pending_my':  my_leaves.filter(status='Pending').count(),
        'approved_my': my_leaves.filter(status='Approved').count(),
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def manage_staff(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    staff_list = User.objects.filter(profile__role='staff')
    return render(request, 'accounts/manage_staff.html', {
        'staff_list':    staff_list,
        'pending_badge': _pending_badge(),
    })


@login_required
def add_staff(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = User.objects.create_user(username=username, password=password)
        profile.objects.create(user=user, role='staff')
        return redirect('manage_staff')
    return render(request, 'accounts/add_staff.html', {
        'pending_badge': _pending_badge(),
    })


@login_required
def edit_staff(request, id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    staff = get_object_or_404(User, id=id)
    if request.method == 'POST':
        staff.username = request.POST['username']
        password = request.POST.get('password', '').strip()
        if password:
            staff.set_password(password)
        staff.save()
        return redirect('manage_staff')
    return render(request, 'accounts/edit_staff.html', {
        'user':          staff,
        'pending_badge': _pending_badge(),
    })


@login_required
def delete_staff(request, id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('manage_staff')