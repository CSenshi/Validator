from validator.rules import Mail


def test_mail_01():
    rule = Mail()
    emails = ["nikalosa@gmail.com", "abgdev@aa.bl", "zz.zz@zz.zz"]

    for email in emails:
        assert rule.check(email)


def test_mail_02():
    rule = Mail()
    emails = ["pochxu@gmail", "ankitrai326.com", "zz@.z"]

    for email in emails:
        assert not rule.check(email)
