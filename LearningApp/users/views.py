from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Du hast dich erfolgreich registriert { username } und kannst dich jetzt einloggen.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":  # Sind Daten da?
        u_form = UserUpdateForm(request.POST, instance=request.user)  # neue Daten kommen
        p_form = ProfileUpdateForm(
                                request.POST,
                                request.FILES,  # neue Bilder kommen
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():  # Sind Daten valide? Wenn ja: speichern
            u_form.save()
            p_form.save()
            messages.success(request, "Profil erfolgreich aktualisiert!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # ans Template übergeben
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


def passwort_reset_done(request):
    messages.success(request, "Du hast dein Passwort erfolgreich zurückgestzt! Du kannst dich jetzt einloggen.")
    return redirect('login')