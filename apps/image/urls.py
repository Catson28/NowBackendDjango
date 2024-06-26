from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas às imagens
    path("add/", views.add_image),  # Adiciona uma nova imagem
    path("view/<int:image_id>/", views.view_image),  # Visualiza uma imagem
    path("delete/<int:image_id>/", views.delete_image),  # Deleta uma imagem
    path(
        "associate-with-service/", views.associate_image_with_service
    ),  # Associa uma imagem a um produto
    path(
        "list-by-type/", views.list_images_by_type
    ),  # Lista imagens por tipo (Produto ou Material bruto)
    path(
        "update-description/<int:image_id>/", views.update_image_description
    ),  # Atualiza a descrição de uma imagem
    path('upload-image/category/', views.UploadCategoryImageView, name='upload_category_image'),
    path('upload-image/service/', views.UploadServiceImageView, name='upload_service_image'),
]
