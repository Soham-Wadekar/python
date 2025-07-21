from django.shortcuts import render

posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "This is the first blog post",
        "date_posted": "July 17, 2025",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "This is the second blog post",
        "date_posted": "July 2, 2025",
    },
    {
        "author": "John Doe",
        "title": "Blog Post 3",
        "content": "This is the third blog post",
        "date_posted": "July 19, 2024",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
