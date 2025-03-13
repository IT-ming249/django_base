from django import forms
from django.core.validators import RegexValidator
from .models import Article


#留言板的表单
class MessageBoardForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=20,label='标题',
                            error_messages={
                                "min_length":"标题最小长度为2",
                                "max_length":"标题最大长度为20！"
                            })
    #widget=forms.Textarea表示多行
    content = forms.CharField(widget=forms.Textarea,label="内容")
    email = forms.EmailField(label="邮箱")


class RegisterForm(forms.Form):
    #validators是验证器，可以是多个  RegexValidator为正则表达式验证器
    telephone = forms.CharField(validators=[RegexValidator(r'1[345678]\d{9}',
                                                           message="请输入正确格式的手机号码")])
    pwd1 = forms.CharField(min_length=6,max_length=100)
    pwd2 = forms.CharField(min_length=6,max_length=100)
    #clean_字段名   自定义字段的验证方法
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # 从数据库中查找telephone是否存在，如果存在，那么抛出验证错误
        if telephone == '18888888888':
            raise forms.ValidationError('手机号码已经存在！')
        else:
            return telephone

    #重写clean方法，自定义某几个字段的验证规则
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码不一致！")
        else:
            return cleaned_data


##ModelForm 使用数据库的字段创建验证表单
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'    #表示继承Article中的所有字段
        #fields = ["title","content"]  #指定继承字段
        #exculde = ["category"]  #排除字段
        #自定义错误消息
        error_messages = {
            "category":{
                "required":"类型不能为空"
            }
        }