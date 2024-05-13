from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import acceuil, register, custom_logout, custom_login, detail_article, commenter_article, like_article, dislike_article, get_like_status, add_to_cart, view_cart, checkout, process_order, order_confirmation, contact_view, privacy_policy_view, terms_of_use_view, presentation_view, cookies_banner_view, catalogue, create_annonce

urlpatterns = [
    path('', acceuil, name='acceuil'),  # Utilisez directement la fonction 'acceuil' plutôt que 'views.acceuil'
    path('register', register, name='register'),
    path('logout', custom_logout, name='logout'),
    path('login', custom_login, name='login'),
    path('<int:article_id>/', detail_article, name='detail_article'),  # Utilisez directement 'detail_article'
    path('<int:article_id>/commenter/', commenter_article, name='commenter_article'),  # Utilisez directement 'commenter_article'
    path('article/<int:article_id>/like/', like_article, name='like_article'),  # Utilisez directement 'like_article'
    path('article/<int:article_id>/dislike/', dislike_article, name='dislike_article'),  # Utilisez directement 'dislike_article'
    path('<int:article_id>/like_status/', get_like_status, name='get_like_status'),  # Utilisez directement 'get_like_status'
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
    path('contact/', contact_view, name='contact'),
    path('privacy-policy/', privacy_policy_view, name='privacy_policy'),
    path('terms-of-use/', terms_of_use_view, name='terms_of_use'),
    path('presentation/', presentation_view, name='presentation'),
    path('cookies-banner/', cookies_banner_view, name='cookies_banner'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create_annonce/', create_annonce, name='create_annonce'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)