from django.shortcuts import render, redirect, get_object_or_404
from leave.models import Leave
from django.contrib.auth.decorators import login_required


def _pending_badge():
    return Leave.objects.filter(status='Pending').count()


@login_required
def apply_leave(request):
    if request.method == 'POST':
        leave_type = request.POST['leave_type']
        start_date = request.POST['start']
        end_date   = request.POST['end']
        reason     = request.POST['reason']
        Leave.objects.create(
            user=request.user,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status='Pending'
        )
        return redirect('staff_dashboard')
    return render(request, 'leaves/apply_leave.html')


@login_required
def my_leaves(request):
    leaves = Leave.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'leaves/my_leaves.html', {'leaves': leaves})


@login_required
def view_leaves(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    pending_count = _pending_badge()
    leaves = Leave.objects.all().order_by('-start_date')
    return render(request, 'leaves/view_leaves.html', {
        'leaves':        leaves,
        'pending_badge': pending_count,
    })


@login_required
def approve_leave(request, id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    leave = get_object_or_404(Leave, id=id)
    leave.status = 'Approved'
    leave.save()
    return redirect('view_leaves')


@login_required
def reject_leave(request, id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')
    leave = get_object_or_404(Leave, id=id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('view_leaves')