import sqlite3
from config import DB_PATH


def add_post(title: str, content: str) -> None:
    add_post_query = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        add_post_query,
        (title, content),
    )
    
    connection.commit()
    connection.close()

def get_posts():
    get_posts_query = """
    SELECT * FROM posts;
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_posts_query)

    posts = cursor.fetchall()
    
    connection.close()

    print('Вот посты:', posts)

add_post("SQ2", "hello world")

def delete_post(post_id: int) -> None:
    delete_post_query = """
    DELETE FROM posts WHERE post_id = ?
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    connection.close()

    print(f"Удалено постов: {cursor.rowcount}")
    
def get_post(post_id: int) -> None:
    get_post_query = """
    SELECT * FROM posts WHERE post_id = ?
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(get_post_query, (post_id,))
    post = cursor.fetchone()
    connection.close()
    print(f"вот пост с айди: {post_id}", post)



get_post(3)
def update_post(post_id: int, new_title: str, new_content: str) -> None:
    update_post_query = """
    UPDATE posts SET title = ?, content = ? WHERE post_id = ?;
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        update_post_query,
        (
            new_title,
            new_content,
            post_id,
        ),
    )

    update_rows_count = cursor.rowcount

    connection.commit()
    connection.close()

    if update_rows_count == 0:
        return "Пост для обновления не найден"
    else:
        return "Пост обновлен"