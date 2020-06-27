import nox

locations = "src", "tests", "noxfile.py"
nox.options.sessions = "black", "mypy", "tests"


@nox.session(python=["3.8", "3.7"])
def tests(session):
    args = session.posargs or ["-v", "--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.8", "3.8"])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8", "3.7"])
def mypy(session):
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)
