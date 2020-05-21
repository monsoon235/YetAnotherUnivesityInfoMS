<template>
  <div class="index">
    <!-- <div style="height: 60px">
      <span class='font'>欢迎进入本校教师信息管理模块</span>
      <p class='text'>教师是核心，是学校培养学生的人才，管理教师信息，了解教师需求很关键</p>
    </div> -->
    <el-row style="margin: 0 auto;">
      <!--<p class="font">以下是您的个人信息</p>-->
      <div class="searchbox" style="display: inline-block; float: right;">

      </div>
    </el-row>

    <el-table
      :data="tableData"
      stripe
      style="width: 100%">
        <el-table-column
        label="工号"
        prop="teaNum">
      </el-table-column>
      <el-table-column
        label="入职年月"
        prop="inwork_time">
      </el-table-column>
      <el-table-column
        label="电子邮箱"
        prop="teacher_mail">
      </el-table-column>
      <el-table-column
        label="所属专业"
        prop="belong_faculty">
      </el-table-column>
      <el-table-column
        label="职称"
        prop="job_title">
      </el-table-column>
      <el-table-column
        label="身份证件号"
        prop="ID_card">
      </el-table-column>
      <el-table-column
        label="身份证件类型"
        prop="card_type">
      </el-table-column>
      <el-table-column
        label="中文名称"
        prop="chinese_name">
      </el-table-column>
      <el-table-column
        label="性别"
        prop="sex">
      </el-table-column>
      <el-table-column
        label="出生日期"
        prop="born_year">
      </el-table-column>
      <el-table-column
        label="国籍"
        prop="nationality">
      </el-table-column>
      <el-table-column
        label="家庭住址"
        prop="home_addr">
      </el-table-column>
      <el-table-column
        label="家庭邮政编码"
        prop="home_code">
      </el-table-column>
      <el-table-column
        label="家庭电话"
        prop="moblie">
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
        <el-form-item label="工号" prop="teaNum" autocomplete="off" disabled='false'>
          <el-input v-model="form.teaNum" autocomplete="off" placeholder='禁止修改工号'></el-input>
        </el-form-item>
        <el-form-item label="入职年月" prop="inwork_time">
          <el-input autocomplete="off" v-model="form.inwork_time" placeholder='禁止修改入职年月'></el-input>
        </el-form-item>
        <el-form-item label="电子邮箱">
          <el-input v-model="form.teacher_mail" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所属专业" prop="belong_faculty">
          <el-input autocomplete="off" v-model="form.belong_faculty" placeholder='禁止修改所属专业'></el-input>
        </el-form-item>
        <el-form-item label="职称" prop="job_title">
          <el-input autocomplete="off" v-model="form.job_title" placeholder='禁止修改职称'></el-input>
        </el-form-item>
        <el-form-item label="身份证件号">
          <el-input v-model="form.ID_card" autocomplete="off" placeholder='禁止修改身份证件号'></el-input>
        </el-form-item>
        <el-form-item label="身份证件类型">
          <el-input v-model="form.card_type" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="中文名称">
          <el-input autocomplete="off" v-model="form.chinese_name"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
            <el-select style='width: 100%; position: absolute; left: 138px' v-model="form.sex" placeholder="请选择性别">
              <el-option style='height: 80%' label="男" value="男" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="女" value="女" autocomplete="off"></el-option>
              <!--<el-option style='height: 80%' label="保密" value="保密" autocomplete="off"></el-option>-->
            </el-select>
        </el-form-item>
        <el-form-item label="出生日期" prop="born_year">
          <el-input autocomplete="off" v-model="form.born_year"></el-input>
        </el-form-item>
        <el-form-item label="国籍" prop="nationality">
          <el-input autocomplete="off" v-model="form.nationality"></el-input>
        </el-form-item>
        <el-form-item label="家庭住址" prop="home_addr">
          <el-input autocomplete="off" v-model="form.home_addr"></el-input>
        </el-form-item>
        <el-form-item label="家庭邮政编码" prop="home_code">
          <el-input autocomplete="off" v-model="form.home_code"></el-input>
        </el-form-item>
        <el-form-item label="家庭电话">
          <el-input v-model="form.moblie" autocomplete="off"></el-input>
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
  .el-dialog__body {
    padding: 10px 20px;
  }
  .el-input {
    width: 80%
  }
  .el-form-item__label {
    width: 15%
  }
  .el-table-column {
    width: 100%;
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
      delId: '',
      form: {
        teaNum: '',
        inwork_time:'',
        teacher_mail:'',
        belong_faculty:'',
        job_title:'',
        ID_card:'',
        card_type:'',
        chinese_name:'',
        sex: "",
        born_year:'',
        nationality:'',
        home_addr:'',
        home_code:null,
        moblie: null,
      },
      rules: {
        home_code: [
          { type: 'number', message: '邮政编码必须为数字值', trigger: 'blur'}
        ],
        moblie: [
          { type: 'number', message: '号码必须为数字值', trigger: 'blur'}
        ]
      }
    }
  },

  methods: {

    sendRequest(url, opt={}) {
      var _this = this
      this.$http.post(url, opt).then(function (res) {
            if(url === 'http://127.0.0.1:8000/api/teacher/mod') {
          // console.log("编辑用户信息")
              _this.tableData = res.data.data
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
            opt._id = that.editId
            //opt.teacherName = opt.teacherName
            //console.log(opt.teacherName)
            // 修改
            that.sendRequest('http://127.0.0.1:8000/api/teacher/mod',{params: opt})
            }
          that.dialogFormVisible = false
          // that.getAllData()
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    editData(index) {
      // console.log(this.tableData.teacherName)
      const selfData = this.tableData[index]
      //this.editId = selfData._id
      this.dialogFormVisible = true
      this.isEdit = true
      this.form.teaNum = selfData.teaNum
      this.form.inwork_time=selfData.inwork_time
      this.form.teacher_mail=selfData.teacher_mail
      this.form.belong_faculty=selfData.belong_faculty
      this.form.job_title=selfData.job_title
      this.form.ID_card=selfData.ID_card
      this.form.card_type=selfData.card_type
      this.form.chinese_name=selfData.chinese_name
      this.form.sex=selfData.sex
      this.form.born_year=selfData.born_year
      this.form.nationality=selfData.nationality
      this.form.home_addr=selfData.home_addr
      this.form.home_code=selfData.home_code
      this.form.moblie=selfData.moblie
    },


    // 请求所有数据
    getAllData() {
      var _this = this
      this.$http.get('http://127.0.0.1:8000/api/teacher/get').then(function (res) {
        console.log(res)
        var resbody = JSON.parse(response.bodyText)
        if(resbody["code"] == 1)
          _this.$message.error('查询教师失败')
        else
          _this.tableData = res.data
      })
      .catch(function (error) {
        console.log(error)
      })
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

