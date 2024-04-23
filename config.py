#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7028934129:AAGQjoZCH6ur7PFsda1Vvwt9ONAb8cAotuM")
    API_ID = int(os.environ.get("API_ID", "26209173"))
    API_HASH = os.environ.get("API_HASH", "a4d86637bb1b8db35e92196493798279")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5954632422")
