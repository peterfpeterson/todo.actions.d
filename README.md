This is my repository of add-ons for [todo.txt](https://github.com/ginatrapani/todo.txt-cli).

To install add a line to your todo.cfg that points to the actions directory.

```
export TODO_ACTIONS_DIR="/Users/me/todo.actions.d"
```

Extensions
----------

* [again](https://github.com/nthorne/todo.txt-cli-again-addon/blob/master/again) - Marks a task as done, and then adding it again, adjusting due dates and deferral dates if desired.
* [edit](https://github.com/mbrubeck/todo.txt-cli/blob/master/todo.actions.d/edit) - Open `$TODO_DIR/BASENAME.txt` in `$EDITOR`.
* [pri](https://github.com/tonipenya/todo.txt-cli/blob/addons/.todo.actions.d/pri) - For each `ITEM#`, calls the builtin `pri` with priority `PRIORITY`.
* repeat - based on [repeat](https://github.com/drobertadams/todo.txt-cli-addons/tree/master/repeat) and written by me
* futureTasks - `TODOTXT_FINAL_FILTER` written by me
* sortCommand - `TODOTXT_SORT_COMMAND` written by me
