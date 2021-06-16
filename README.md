Issue: SourceFileLoader is loading files from different directories, but the contents of the files are MIXED


Actual results
--------------

```
dir1 ->
TEST1 at dir1/makefile.py Hello
TEST2 at dir1/makefile.py ['World']
TEST3 at dir1/makefile.py First

THIS ONE SHOULD BE EMPTY, TEST1 and TEST2 are not defined in dir1/dir2/makefile.py
dir1/dir2 ->
TEST1 at dir1/dir2/makefile.py Hello
TEST2 at dir1/dir2/makefile.py ['World']
TEST3 at dir1/dir2/makefile.py Overwritten
```


Expected
--------

```
dir1 ->
TEST1 at dir1/makefile.py Hello
TEST2 at dir1/makefile.py ['World']
TEST3 at dir1/makefile.py First

THIS ONE SHOULD BE EMPTY, TEST1 and TEST2 are not defined in dir1/dir2/makefile.py
dir1/dir2 ->
TEST1 at dir1/dir2/makefile.py None
TEST2 at dir1/dir2/makefile.py None
TEST3 at dir1/dir2/makefile.py Overwritten
```
