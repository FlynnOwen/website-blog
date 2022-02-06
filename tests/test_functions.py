import pytest

from app import generate_quote


def test_generate_quote():
    quotes = {
        "\"If a machine is expected to be infallible, it cannot also be intelligent.\" - Alan Turing",
        "\"All models are wrong, but some are useful.",
        "\"I learned very early the difference between knowing the name of something and knowing something.\" - Richard Feynman",
        "\"Talk is cheap. Show me the code.\" - Linus Torsvalds",
        "\"Intelligence is the ability to avoid doing work, yet getting the work done.\" - Linus Torsvalds",
        "\"He became a poet, he lacked imagination for a mathematician.\" - David Hilbert",
        "\"Begin with the simplest examples.\" - David Hilbert",
        "\"To ask the right question is harder than to answer it.\" - Georg Cantor",
        "\"The essence of mathematics lies in it's freedom.\" - Georg Cantor",
        "\"Logic is the foundation of the certainty of all the knowledge we acquire.\" - Leonard Euler",
        "\"Nothing takes place in the world whose meaning is not that of some maximum or minimum.\" - Leonard Euler",
        "\"I have had my results for a long time: but I do not yet know how I am to arrive at them.\" - Carl Friedrich Gauss",
        "\"Computers are like humans, they do everything except think.\" - John Von Neumann",
        "\"All generalisations - perhaps except this one, are false.\" - Kurt Goedel",
        "\"People think that mathematics is complicated. Mathematics is the simple bit. It's cats that are complicated.\" - John Conway"
    }

    quote = generate_quote()

    assert quote in quotes