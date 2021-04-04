> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [97-things-every-x-should-know.gitbooks.io](https://97-things-every-x-should-know.gitbooks.io/97-things-every-programmer-should-know/content/en/thing_43/)

Know How to Use Command-line Tools
==================================

Today, many software development tools are packaged in the form of Integrated Development Environments (IDEs). Microsoft's Visual Studio and the open-source Eclipse are two popular examples, though there are many others. There is a lot to like about IDEs. Not only are they easy to use, they also relieve the programmer of thinking about a lot of little details involving the build process.

今天，许多软件开发工具都以集成开发环境（IDE）的形式打包。微软的Visual Studio和开源的Eclipse是两个流行的例子，尽管还有很多其他的例子。IDE有很多优点。它们不仅易于使用，而且还减轻了程序员对涉及构建过程的许多小细节的思考。



Ease of use, however, has its downside. Typically, when a tool is easy to use, it's because the tool is making decisions for you and doing a lot of things automatically, behind the scenes. Thus, if an IDE is the only programming environment that you ever use, you may never fully understand what your tools are actually doing. You click a button, some magic occurs, and an executable file appears in the project folder.

然而，易用性也有其缺点。通常情况下，当一个工具很容易使用时，是因为这个工具在幕后为你做决策，自动做了很多事情。因此，如果IDE是你唯一使用的编程环境，你可能永远不会完全理解你的工具到底在做什么。你点击一个按钮，一些神奇的事情发生了，一个可执行文件出现在项目文件夹中。



By working with command-line build tools, you will learn a lot more about what the tools are doing when your project is being built. Writing your own make files will help you to understand all of the steps (compiling, assembling, linking, etc.) that go into building an executable file. Experimenting with the many command-line options for these tools is a valuable educational experience as well. To get started with using command-line build tools, you can use open-source command-line tools such as GCC or you can use the ones supplied with your proprietary IDE. **After all, a well-designed IDE is just a graphical front-end to a set of command-line tools.**

通过使用命令行构建工具，你将更多地了解工具在构建项目时的工作。编写自己的make文件将帮助你了解构建可执行文件的所有步骤（编译、组装、链接等）。尝试使用这些工具的许多命令行选项也是一种宝贵的教育经验。要开始使用命令行构建工具，你可以使用开源的命令行工具，如GCC，也可以使用专有IDE提供的工具。毕竟，一个精心设计的IDE只是一套命令行工具的图形化前端。



In addition to improving your understanding of the build process, there are some tasks that can be performed more easily or more efficiently with command-line tools than with an IDE. For example, the search and replace capabilities provided by the _grep_ and _sed_ utilities are often more powerful than those found in IDEs. Command-line tools inherently support scripting, which allows for the automation of tasks such as producing scheduled daily builds, creating multiple versions of a project, and running test suites. In an IDE, this kind of automation may be more difficult (if not impossible) to do as build options are usually specified using GUI dialog boxes and the build process is invoked with a mouse click. If you never step outside of the IDE, you may not even realize that these kinds of automated tasks are possible.

除了提高对构建过程的理解外，有些任务可以通过命令行工具比IDE更容易或更有效地执行。例如，_grep_和_sed_实用程序提供的搜索和替换功能通常比IDE中的功能更强大。命令行工具本身就支持脚本，这使得任务的自动化成为可能，例如生成预定的日常构建、创建一个项目的多个版本以及运行测试套件。在IDE中，这种自动化可能会比较困难（如果不是不可能的话），因为构建选项通常是通过GUI对话框来指定的，而且构建过程是通过鼠标点击来调用的。如果你从来没有离开过IDE，你可能甚至没有意识到这些类型的自动化任务是可能的。



But wait. Doesn't the IDE exist to make development easier, and to improve the programmer's productivity? Well, yes. The suggestion presented here is not that you should stop using IDEs. The suggestion is that you should **"look under the hood"**（从头看，看看基础，看一下底层， 经常看到英文技术文章里有这个短语。查了一下，原来英文里有一个常用短语，叫做"under the hood"，钻进魔术师的帐篷，屏住呼吸，瞪大眼睛，把那些奇妙的魔法看个通透，让自己的理解和技艺获得巨幅的提升。所以这个短语意思就是“深入。。。”） and understand what your IDE is doing for you. The best way to do that is to learn to use command-line tools. Then, when you go back to using your IDE, you'll have a much better understanding of what it is doing for you and how you can control the build process. On the other hand, once you master the use of command-line tools and experience the power and flexibility that they offer, you may find that you prefer the command line over the IDE.

但是，等等，IDE的存在不就是为了让开发更简单，提高程序员的工作效率吗？IDE的存在不就是为了让开发更容易，提高程序员的工作效率吗？嗯，是的。这里提出的建议不是说你应该停止使用IDE。我们的建议是，你应该 "从头看起"，了解你的IDE在为你做什么。最好的方法是学习使用命令行工具。然后，当你再去使用你的IDE时，你会对它为你做了什么以及如何控制构建过程有更好的理解。另一方面，一旦你掌握了命令行工具的使用，并体验到它们所提供的强大和灵活性，你可能会发现你更喜欢命令行而不是IDE。

By [Carroll Robinson](http://programmer.97things.oreilly.com/wiki/index.php/Carroll_Robinson)
