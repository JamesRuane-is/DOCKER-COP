import psycopg2
import redis


def test_postgres_seeded():
    conn = psycopg2.connect(
        host="db", user="app", password="secret", dbname="appdb"
    )
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users;")
    assert cur.fetchone()[0] == 3
    conn.close()


def test_redis_roundtrip():
    r = redis.Redis(host="cache", port=6379)
    r.set("ping", "pong")
    assert r.get("ping") == b"pong"
