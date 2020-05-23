<template>
  <div class="register">
    <LoginHeader></LoginHeader>
    <div class="from">
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="请输入用户名" prop="id">
          <el-input type="text" v-model="ruleForm.id" label="输入学号,教职工号或是admin"></el-input>
        </el-form-item>
        <el-form-item label="请输入密码" prop="pass">
          <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-form-item>
            <el-button type="info" @click="submitForm('ruleForm')">登录</el-button>
            <el-button type="info" @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style lang='scss'>
// @import 'element-ui/lib/theme-chalk/index.css';
.from {
  margin: 0px auto;
  width: 500px;
  .el-select, .el-form-item {
    width: 100%;
    .el-input {
      width: 400px;
    }
  }
  button {
    width: 70px;
    height: 40px;
    margin-right: 20px;
    background-color: #3C8EC0;
    box-shadow: none;
    border: 1px solid #3c60c9;
    border-radius: 5px;
    font-size: 14px;
    color: #fff;
  }

}
</style>

<script>
import LoginHeader from '../components/LoginHeader';

export default {
    components: { LoginHeader },
    data() {
      var checkName = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入用户名'))
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass')
          }
          callback();
        }
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass')
          }
          callback()
        }
      };
      return {
        ruleForm: {
          pass: '',
          id: '',
        },
        rules: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          id : [
            { validator: checkName, trigger: 'blur' },
            { message: '请输入用户名称', trigger: 'blur' },
            { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
          ]
        }
      }
    },
    methods: {

    submitForm(formName) {
        this.$refs[formName].validate((valid) => {
            if (valid) {
              let params = {
                id: this.ruleForm.id,
                password: this.ruleForm.pass,
              }
              // console.log(params);
              this.$http.post('/api/login', params)
                .then((res) => {
                  var _this = this
                  // console.log(res)
                  // console.log(res.data.data[0]);
                  if(res.data.code == 0) {
                    console.log(res.data)
                    return
                  }

                  else if (res.data.code == 1) {
                      alert('登录成功');
                      // console.log(res.data.type)
                      try {
                        switch(res.data.type) {
                          case 2:
                            setTimeout(() => this.$router.push({ path:'/student/start'}), 800)
                            break;
                          case 1:
                            setTimeout(() => this.$router.push({ path:'/teacher/start'}), 800)
                            break;
                          case 0:
                            setTimeout(() => this.$router.push({ path:'/manager/start'}), 800)
                            break;
                          localStorage.setItem("id", JSON.stringify(res.data.id));
                        }
                      }
                      catch(err) {
                          console.log(err)
                          alert('对不起，登录失败，请重新尝试');
                      }
                  }else{
                      alert('用户名不存在或密码错误，您无法登陆！')
                  }
              }).catch((err)=>{
                  console.log(err)
              })
            } else {
            console.log('error submit!!')
            return false
            }
        });
    },
    resetForm(formName) {
        this.$refs[formName].resetFields()
    }
  }
}
</script>
