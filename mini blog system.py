import datetime

class BlogSystem:
    def __init__(self):
        self.posts = []

    def display_posts(self):
        print("\nBlog Posts:")
        if not self.posts:
            print("No posts yet.")
        else:
            for post in self.posts:
                print(f"\nTitle: {post['title']}")
                print(f"Author: {post['author']}")
                print(f"Date: {post['date']}")
                print(f"Content: {post['content']}")

    def add_post(self, title, author, content):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post = {'title': title, 'author': author, 'date': date, 'content': content}
        self.posts.append(post)
        print("Post added successfully.")

def main():
    blog_system = BlogSystem()

    while True:
        print("\nOptions:")
        print("1. Display Blog Posts")
        print("2. Add Blog Post")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            blog_system.display_posts()
        elif choice == '2':
            title = input("Enter the post title: ")
            author = input("Enter the author's name: ")
            content = input("Enter the post content: ")
            blog_system.add_post(title, author, content)
        elif choice == '3':
            print("Exiting the Blog System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
