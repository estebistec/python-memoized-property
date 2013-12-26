=================
memoized_property
=================

.. image:: https://badge.fury.io/py/memoized-property.png
    :target: http://badge.fury.io/py/memoized-property
    
.. image:: https://travis-ci.org/estebistec/python-memoized-property.png?branch=master
        :target: https://travis-ci.org/estebistec/python-memoized-property

.. image:: https://pypip.in/d/memoized-property/badge.png
        :target: https://crate.io/packages/memoized-property?version=latest


A simple python decorator for defining properties that only run their fget function once.

* Free software: BSD license

What?
-----

A Python property that only calls its ``fget`` function one time. How many times have you written
this code (or similar)?

::

    def class C(object):

        @property
        def name(self):
            if not hasattr(self, '_name'):
                self._name = some_expensive_load()
            return self._name

I've written it just enough times to be annoyed enough to capture this module. The result is this::

    from memoized_property import memoized_property

    def class C(object):

        @memoized_property
        def name(self):
            # Boilerplate guard conditional avoided, but this is still only called once
            return some_expensive_load()

Why?
----

I couldn't find a pre-existing version of this on PyPI. I found one other on GitHub,
https://github.com/ytyng/python-memoized-property, but it was not published to PyPI.
