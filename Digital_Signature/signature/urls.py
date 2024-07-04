from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
import uuid

from django.urls import path
from .views import (
    LoanProcessView, ViewOriginalDocumentView, SignAgreementView,
    SignAgreementSuccessView, ViewSignedAgreementView
)

urlpatterns = [
    path('loan_process/', LoanProcessView.as_view(), name='loan_process'),
    path('view_original_document/<uuid:agreement_id>/<uuid:borrower_id>/', ViewOriginalDocumentView.as_view(), name='view_original_document'),
    path('sign_agreement/<uuid:agreement_id>/<uuid:borrower_id>/', SignAgreementView.as_view(), name='sign_agreement'),
    path('sign_agreement_success/<uuid:agreement_id>/<uuid:borrower_id>/', SignAgreementSuccessView.as_view(), name='sign_agreement_success'),
    path('view_signed_agreement/<uuid:agreement_id>/<uuid:borrower_id>/', ViewSignedAgreementView.as_view(), name='view_signed_agreement'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)