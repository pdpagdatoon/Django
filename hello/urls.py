from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<slug:slug>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("preview/audiomixer/", views.audiomixer_page, name="preview-audiomixer"),
    path("preview/earbuds/", views.earbuds_page, name="preview-earbuds"),
    path("preview/jackcable/", views.jackcable_page, name="preview-jackcable"),
    path("preview/compacteddisc/", views.compacteddisc_page, name="preview-compacteddisc"),
    path("preview/cdplayer/", views.cdplayer_page, name="preview-cdplayer"),
    path("preview/drums/", views.drums_page, name="preview-drums"),
    path("preview/guitar/", views.guitar_page, name="preview-guitar"),
    path("preview/piano/", views.piano_page, name="preview-piano"),
]
