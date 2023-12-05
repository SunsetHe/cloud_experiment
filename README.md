# cloud_experiment

---------------------------

1.关于代码，仓库中会存放一个名为sort.py的python代码，该代码会生成乱序且不重复的0-9的个位整数，然后代码将他们通过选择排序从小到大排序，输出排序之后的这10个数，将这十个数放入并上传到工作流中$GITHUB_WORKSPACE中一个名为sorted.txt的文件中

2.当仓库发生push或者pr并合并之后，工作流会使用Ubuntu环境，并安装python3，然后使用python运行第一步的代码，第一步的工作流产生的sorted.txt需要保留下来，作为工作流第二步的所需要的文件

3.接下来工作流会进入第二步测试的工作流，工作流会使用Ubuntu环境，并安装python3，然后运行仓库中的名为test.py的python代码，测试的工作流会运行测试代码，测试代码会读入第一步工作流输出并保留的sorted.txt并检测其中的数是否按从小到大排序，如果是，那么工作流通过，并输出"sort succeed"如果不是，那么仓库流不通过

