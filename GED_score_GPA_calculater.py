#asking user input for score
social=int(input('please enter your social score'))
math=int(input('please enter your math score'))
RLA=int(input('please enter your  RLA score'))
science=int(input('please enter your science score'))
total_average_score=int((social+math+RLA+science))
print('total average score',total_average_score)
#output of score base on user's input
if total_average_score>0 and total_average_score <450:
   print('fail')
elif total_average_score>=700 and   total_average_score<=800:
   print('distinction')
elif total_average_score>=600 and total_average_score<=700:
   print('merit')
elif total_average_score>=450 and total_average_score<=500:
   print('pass')
else:
   print('please try again')
#convert onto GPA score
print('enter yes for GPA')
print('enter no for end')
position=input('yes or no')
position=position.lower()
if position== 'yes':
   GPA=int(input("please enter your total score to notary GPA"))
   Maximun_score=800
   GPA=int((total_average_score/ Maximun_score)*4 )
   if GPA>0:
     print('your GPA is',GPA)
   else:
      print('error try again')
else: position=='no'
print('Thank you for Using Our Service')

