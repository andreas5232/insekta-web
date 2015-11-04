from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Certificate, SignError
from .forms import CreateCertificateForm


@login_required
def index(request):
    certificates = list(Certificate.objects.filter(user=request.user))
    has_valid_certificate = False
    for certificate in certificates:
        if certificate.is_valid:
            has_valid_certificate = True
            break
    certificates.sort(key=lambda cert: (cert.is_valid, cert.expires))
    return render(request, 'pki/index.html', {
        'certificates': certificates,
        'has_valid_certificate': has_valid_certificate
    })

@login_required()
def create_certificate(request):
    error = None
    if request.method == 'POST':
        form = CreateCertificateForm(request.POST)
        if form.is_valid():
            csr_pem = form.cleaned_data['csr_pem']
            try:
                Certificate.create_from_csr(request.user, csr_pem)
            except SignError as e:
                error = str(e)
            else:
                return redirect('pki:index')
    else:
        form = CreateCertificateForm()

    return render(request, 'pki/create_certificate.html', {
        'form': form,
        'error': error
    })

@require_POST
@login_required
def revoke_certificate(request):
    fingerprint = request.POST.get('fingerprint', '')
    cert = get_object_or_404(Certificate, fingerprint=fingerprint,
                                          user=request.user)
    if 'really' in request.POST:
        cert.revoke()
        return redirect('pki:index')
    return render(request, 'pki/revoke_certificate.html', {
        'certificate': cert
    })