import requests
import json

API_URL = 'http://localhost:8000/api/blog/'

blogs = [
    {
        "title": "Getting Started with Django REST Framework",
        "slug": "getting-started-with-django-rest-framework",
        "excerpt": "Learn how to build powerful APIs using Django REST Framework with best practices.",
        "content": "Django REST Framework is a powerful and flexible toolkit for building Web APIs. In this tutorial, we will explore the basics of DRF and how to create a simple API. We will cover serializers, viewsets, routers, and authentication. By the end of this guide, you will have a solid understanding of how to build scalable APIs with Django.",
        "tags": "Django, REST API, Python, Backend",
        "published": True,
        "order": 1
    },
    {
        "title": "Building Modern Web Interfaces with Next.js 15",
        "slug": "building-modern-web-interfaces-with-nextjs-15",
        "excerpt": "Discover how to create blazing-fast web applications with Next.js 15 and React.",
        "content": "Next.js 15 brings significant improvements to the React ecosystem. With features like Server Components, automatic optimization, and built-in routing, building modern web interfaces has never been easier. This post covers the key features of Next.js 15, including the new App Router, Incremental Static Regeneration (ISR), and how to integrate it with your backend API.",
        "tags": "Next.js, React, Frontend, JavaScript",
        "published": True,
        "order": 2
    },
    {
        "title": "Understanding Full-Stack Development",
        "slug": "understanding-full-stack-development",
        "excerpt": "A comprehensive guide to becoming a full-stack developer in 2024.",
        "content": "Full-stack development encompasses both frontend and backend development. This article explores the essential skills needed to become a full-stack developer, including frontend frameworks like React and Next.js, backend frameworks like Django and Node.js, databases, and deployment strategies. We will also discuss best practices for building scalable applications.",
        "tags": "Full-Stack, Development, Career, Web Development",
        "published": True,
        "order": 3
    }
]

for blog in blogs:
    response = requests.post(API_URL, json=blog)
    if response.status_code == 201:
        print(f"✓ Created: {blog['title']}")
    else:
        print(f"✗ Failed: {blog['title']} - {response.text}")

print("\nVerifying created blogs...")
response = requests.get(API_URL)
print(f"Total blogs: {len(response.json()) if isinstance(response.json(), list) else response.json()['count']}")