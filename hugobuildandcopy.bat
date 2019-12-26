rmdir /s public
y
hugo
set src="public"
set des="..\..\arbanhossain.github.io\blog"
xcopy /s "%src%" "%des%"
a