from home.models import Category, Post

category_all = Category(name="All")


def get_category_and_posts(category_name):
    posts = Post.objects.filter(published=True)
    if category_name == category_all.slug():
        category = Category(name=category_name)
    else:
        try:
            category = Category.objects.get(name__iexact=category_name)
            posts = posts.filter(category=category)
        except Category.DoesNotExist:
            category = Category(name=category_name)
            posts = Post.objects.none()

    posts = posts.order_by('-created_at')
    return category, posts


# def get_categories():
#    categories = list(Category.objects.all().order_by('name'))
#    categories.insert(0, category_all)
#    return categories
