
def upload_movie_image(instance, filename):
    return f'movies/{instance.category.slug}/{filename}'