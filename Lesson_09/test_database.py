from sqlalchemy import create_engine
from sqlalchemy.sql import text


db = create_engine(
    'postgresql://postgres:bloodsweat&tears@localhost:5432/Practice'
    )


def test_get_max_subject():
    sql_statement = text(
        "SELECT max(subject_id) FROM subject"
        )
    assert db.execute(sql_statement).fetchone()[0] == 16
    db.execute(sql_statement)


def test_subject_title():
    sql_statement = text(
        "SELECT subject_id FROM subject WHERE subject_title = 'Art'"
        )
    assert db.execute(sql_statement).rowcount == 0
    db.execute(sql_statement)


def test_insert_into_subject():
    sql_statement = text(
        "insert into subject values (17, 'Art')"
        )
    db.execute(sql_statement)
    sql_statement2 = text(
        "SELECT subject_title FROM subject WHERE subject_id = 17"
        )
    assert db.execute(sql_statement2).fetchone()[0] == 'Art'
    sql_statement = text(
        "delete from subject where subject_id = 17"
        )
    db.execute(sql_statement)


def test_update_subject():
    sql_statement = text(
        "insert into subject values (17, 'Art')"
    )
    db.execute(sql_statement)
    sql_statement2 = text(
        "update subject set subject_title = 'Music' where subject_id = 17"
    )
    db.execute(sql_statement2)
    sql_statement3 = text(
        "SELECT subject_title FROM subject WHERE subject_id = 17"
    )
    assert db.execute(sql_statement3).fetchone()[0] == 'Music'
    sql_statement = text(
        "delete from subject where subject_id = 17"
    )
    db.execute(sql_statement)


def test_delete_subject():
    sql_statement = text(
        "insert into subject values (17, 'Art')"
    )
    db.execute(sql_statement)
    sql_statement2 = text(
        "SELECT subject_title FROM subject WHERE subject_id = 17"
    )
    assert db.execute(sql_statement2).fetchone()[0] == 'Art'
    sql_statement = text(
        "delete from subject where subject_id = 17"
    )
    db.execute(sql_statement)
    sql_statement2 = text(
        "SELECT subject_title FROM subject WHERE subject_id = 17"
    )
    assert db.execute(sql_statement2).rowcount == 0
    db.execute(sql_statement)
