<template>
  <div class="index">   
    
    <el-row style="margin: 0 auto;">
      <p class="font">以下是您的个人信息</p>
    </el-row>
    <el-table
      :data="tableData"
      stripe
      style="width: 100%">
   		<el-table-column
        prop="id"
        label="学号">
      </el-table-column>
      <el-table-column
        label="证件类型">
        <template slot-scope="scope">
          <i v-if="scope.row.person_id_type==0">身份证</i>
          <i v-else>护照</i>
        </template>
      </el-table-column>
      <el-table-column
        prop="person_id"
        label="证件号">
      </el-table-column>
      <el-table-column
        prop="person_name"
        label="姓名">
      </el-table-column>
      <el-table-column
        label="性别">
        <template slot-scope="scope">
          <i v-if="scope.row.gender==0">男</i>
          <i v-else>女</i>
        </template>
      </el-table-column>
      <el-table-column
        prop="birth"
        label="出生日期">
      </el-table-column>
      <el-table-column
        prop="country"
        label="国籍">
      </el-table-column>
      <el-table-column
        prop="family_address"
        label="家庭住址">
      </el-table-column>
      <el-table-column
        prop="family_zipcode"
        label="邮政编码">
      </el-table-column>
      <el-table-column
        prop="family_tel"
        label="家庭电话">
      </el-table-column>
      <el-table-column
        prop="age"
        label="年龄">
      </el-table-column>
      <el-table-column
        prop="email"
        label="邮箱">
      </el-table-column>
      <el-table-column
        prop="enroll_date"
        label="入学日期">
      </el-table-column>
      <el-table-column
        prop="class_name"
        label="班级">
      </el-table-column>
       <el-table-column
        label="操作">
        <template slot-scope="scope">
          <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
         </template>
      </el-table-column>

    </el-table>


    <el-dialog title="填写你的信息" :visible.sync="dialogFormVisible" style="height: 100%">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="姓名" prop="person_name">
          <el-input v-model="form.person_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="证件类型">
          <el-select style="width:85%" v-model="form.person_id_type" placeholder="请选择证件类型">
            <el-option label="身份证" value="0" autocomplete="off"></el-option>
            <el-option label="护照" value="1" autocomplete="off"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="证件号" prop="person_id">
            <el-input v-model="form.person_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别">
            <el-select style="width:85%" v-model="form.gender" placeholder="请选择性别">
              <el-option label="男" value="0" autocomplete="off"></el-option>
              <el-option label="女" value="1" autocomplete="off"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="出生日期">
          <el-input v-model="form.birth" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="国籍">
          <el-input v-model="form.country" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="家庭住址">
          <el-input v-model="form.family_address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮政编码">
          <el-input v-model="form.family_zipcode" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="家庭电话">
          <el-input v-model="form.family_tel" autocomplete="on"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="form.email" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitFrom">确 定</el-button>
      </div>
    </el-dialog>

    
  </div>
</template>

<style lang='scss'>
  @import "../../static/css/base.scss";
  .font {
    @include fontTwo()
  }
  .text {
    @include fontThree()
  }
  .el-input {
    width: 80%
  }
  .el-form-item__label {
    width: 15%
  }
</style>

<script>
export default {
  name: "index",
  data() {
    return {
      dialogVisible:false,
      tableData: [],
      dialogFormVisible: false,
      isEdit: false, //是否修改
      editId: '',
      // delId: '',
      form: {
        person_id_type: '',
        person_id: '',
        person_name: "",
        person_gender: "",
        person_birth: '',
        person_country: '',
        person_family_address: '',
        person_family_zipcode: '',
        person_family_tel: '',
        email: '',
        enroll_date: '',
        class_name: '',
      },
      rules: {
        name: [
          { required: true, message: '必填', trigger: 'blur' },
          { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
        ],
        person_id_type: [
          {required: true, message: '必填', trigger: 'blur' },
        ],
        person_id: [
          {required: true, message: '必填', trigger: 'blur' },
        ],
        birth: [
          {required: true, message: '必填', trigger: 'blur' },
        ],
        country: [
          {required: true, message: '必填', trigger: 'blur' },
        ],
        family_address:  [
          {required: true, message: '必填', trigger: 'blur' },
        ],
        family_zipcode:  [
          {required: true, message: '必填', trigger: 'blur' },
        ],
      }
    }
  },

  methods: {
    sendRequest(url, opt={}) {
      var _this = this
      _this.$http.post(url, opt).then(function (res) {
        if(url === '/api/student/mod') {
          // console.log("编辑用户信息")
          _this.tableData[0] = res.data.list
        } 
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    submitFrom() {
      const that = this
      this.$refs['form'].validate((valid) => {
        if (valid) {
          if(that.isEdit) {
            let opt = that.form
            // opt._id = that.editId
            // 修改
              that.sendRequest('/api/student/mod',{"where":{"id":this.editId},"update":opt})
            }      
          that.dialogFormVisible = false
        } else {
          console.log('error submit!!');
          return false;
        }
      });

      
    },

    // 请求所有数据
    getAllData() {
      // console.log(this.form.className.age)
      var _this = this
      // console.log(JSON.parse(window.localStorage.stuInfo).username)
      this.$http.get('/api/student/get',{params:{id:localStorage['id']}}).then(function (res) {
        if(res.data.list.length === 0||res.data.code ==0) {
            alert('该系统还没有您的个人信息，请联系教学管理员');
            return;
        }
        _this.tableData=res.data.list
        this.dataFit()
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    dataFit(){
      var mydate=new Date()
      var year=mydate.getFullYear()
      for(var i=0;i<this.tableData.length;i++){
        this.tableData[i].birth=this.tableData[i].birth.slice(0,10)
        this.tableData[i].age=(year-this.tableData[i].birth.slice(0,4))
        this.tableData[i].enroll_date=this.tableData[i].enroll_date.slice(0,10)
      }
    },
    editData(index) {
      const selfData = this.tableData[index]
      // this.editId = selfData._id
      this.dialogFormVisible = true
      this.isEdit = true
      this.editId = selfData.id
      this.form.person_id = selfData.person_id
      this.form.person_id_type = selfData.person_id_type
      this.form.person_name = selfData.person_name
      this.form.gender = selfData.gender
      this.form.birth = selfData.birth
      this.form.country = selfData.country
      this.form.family_address = selfData.family_address
      this.form.family_zipcode = selfData.family_zipcode
      this.form.family_tel = selfData.family_tel
      this.form.email = selfData.email
      this.form.enroll_date = selfData.enroll_date
      this.form.class_name = selfData.class_name
    },
  },

  watch: {
    dialogFormVisible() {
      if(!this.dialogFormVisible) this.isEdit=false
    }
  },
  mounted: function() {
    // 组件创建时候去获取所有的用户数据
    this.getAllData();
  }

  
};
</script>

