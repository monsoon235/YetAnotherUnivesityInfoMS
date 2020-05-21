<template>
  <div>
    <!-- <div style="height: 90px">
      <span class='font'>欢迎进入本校班级管理模块</span>
      <p class='text'>尊敬的管理员您好，班级的存在与设置记录了学校的成长，您只可以进行查询、增加、修改，请谨慎操作(如勿操作，请联系后台管理员)</p>
    </div> -->
    <div>
	    <el-row>
        <el-button type="primary" @click="dialogFormVisible = true">新增</el-button>
	      <div class="searchbox" style="display: inline-block; float: right;">
	        <!--<input class="sc" type="text" placeholder="请输入课程号" style="width: 300px; margin-right: 20px; height: 32px; border-radius: 1px solid #302d1c; margin-bottom: -3px; position: relative; top: 3px;"/>-->
          <el-button type="warning" plain @click="show1 = !show1">展开</el-button>
          <el-button type="danger" plain @click="getAllData()">刷新</el-button>
          <el-button type="danger" plain @click="add_test()">测试</el-button>
	      </div>
		  </el-row>
      <el-collapse-transition>
        <div v-if="show1">
          <br>
          <el-form :inline="true" :model="form" :rules="searchRules" ref="form" label-width="100px" class="demo-ruleForm">
          <el-form-item label="开课号" prop="id">
            <el-input v-model="form.id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程号" prop="course_id">
            <el-input v-model="form.course_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程名称" prop="course_name">
            <el-input v-model="form.course_name" autocomplete="off"></el-input>
          </el-form-item>
          <!--<el-form-item label="开课专业" prop="major_name">
            <el-input v-model="form.major_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="考核方式" prop="assessment">
            <el-input v-model="form.assessment" autocomplete="off" placeholder="考试或当堂答辩"></el-input>
          </el-form-item>-->
          <el-form-item label="老师工号" prop="teacher_id">
            <el-input v-model="form.teacher_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="授课老师" prop="teacher_name">
            <el-input v-model="form.teacher_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课日期" prop="year">
            <el-input v-model="form.year" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="term">
            <el-select  v-model="form.term" placeholder="请选择学期">
              <el-option style='height: 80%' label="春" value="春" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="秋" value="秋" autocomplete="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开课时间" prop="time">
            <el-input v-model="form.time" autocomplete="off" placeholder="周一至周五的第一到第九节"></el-input>
          </el-form-item>
            <el-form-item>
          <el-button type="primary" plain @click="mysearch">搜索</el-button>
        </el-form-item>
        </el-form>

        </div>
      </el-collapse-transition>
			<el-table
	      :data="tableData"
	      stripe
	      style="width: 100%">
	      <el-table-column
	        prop="course_id"
	        label="课程号">
	      </el-table-column>
	      <el-table-column
	        prop="course_name"
	        label="课程名称">
	      </el-table-column>
          <el-table-column
	        prop="major_name"
	        label="开课专业">
	      </el-table-column>
          <el-table-column
	        prop="assessment"
	        label="考核方式">
	      </el-table-column>
	      <el-table-column
	        prop="teacher_name"
	        label="授课老师">
	      </el-table-column>
	      <el-table-column
	        prop="year"
	        label="开课日期">
	      </el-table-column>
	      <el-table-column
	        prop="term"
	        label="开课学期">
	      </el-table-column>
	      <el-table-column
	        prop="time"
	        label="开课时间">
	      </el-table-column>
	       <el-table-column
	        label="操作">
	        <template slot-scope="scope">
	          <el-button type="primary" @click="editData(scope.$index)">修改</el-button>
	          <el-button type="danger" @click="openDialog(scope.$index)">删除</el-button>
	        </template>
	      </el-table-column>
	    </el-table>

    <div style="margin-top: -60px">
      <el-dialog title="请填写开课信息" :visible.sync="dialogFormVisible" style="height: 100%；">
        <el-form :model="form" :rules="rules" ref="form">
          <el-form-item label="开课号" prop="id">
            <el-input v-model="form.id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程号" prop="course_id">
            <el-input v-model="form.course_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程名称" prop="course_name">
            <el-input v-model="form.course_name" autocomplete="off"></el-input>
          </el-form-item>
          <!--<el-form-item label="开课专业" prop="major_name">
            <el-input v-model="form.major_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="考核方式" prop="assessment">
            <el-input v-model="form.assessment" autocomplete="off" placeholder="考试或当堂答辩"></el-input>
          </el-form-item>-->
          <el-form-item label="老师工号" prop="teacher_id">
            <el-input v-model="form.teacher_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="授课老师" prop="teacher_name">
            <el-input v-model="form.teacher_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课日期" prop="year">
            <el-input v-model="form.year" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="term">
            <el-select  v-model="form.term" placeholder="请选择学期">
              <el-option style='height: 80%' label="春" value="春" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="秋" value="秋" autocomplete="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开课时间" prop="time">
            <el-input v-model="form.time" autocomplete="off" placeholder="周一至周五的第一到第九节"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="submitFrom">确 定</el-button>
        </div>
      </el-dialog>
    </div>

	    <el-dialog
	      title="提示"
	      :visible.sync="dialogVisible"
	      width="30%">
	      <span>确定要删除信息</span>
	      <span slot="footer" class="dialog-footer">
	        <el-button @click="dialogVisible = false">取 消</el-button>
	        <el-button type="primary" @click="delData">确 定</el-button>
	      </span>
    	</el-dialog>
		</div>
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
      dialogVisible: false,
      tableData: [],
      dialogFormVisible: false,
      dialogFormSearch: false,
      isEdit: false, //是否修改
      show1:false,
      editId: '',
      delId: '',
      form: {
      id:'',
      course_id:'',
	    course_name:'',
	    //major_name:'',
      //assessment:'',
      teacher_id:'',
	    teacher_name:'',
	    year:'',
	    term:'',
	    time:''
      },
      rules:{
      },
      searchRules: {

      },
  }},
methods: {
    add_test(){
      var _this=this
      this.$http.post('http://127.0.0.1:8000/api/teacher/add',{'id':'123','person_id':'1231313','enroll_date':'1111-11-11', 'email':'12',
       'title':'23', 'major_id':'32', 'person_id':'1'}).then(function (res) {
          console.log(res)
          _this.tableData.push(res.data)
        })
        .catch(function (error) {
          console.log(error)
        })
      this.$http.post('http://127.0.0.1:8000/api/lecture/add',{'id':'1','course_id':'12', 'teacher_id':'23', 'year':'1992',
      'term':'1', 'time':'2'}).then(function (res) {
          console.log(res)
          _this.tableData.push(res.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },



		// 获取所有的用户信息
    getAllData() {
      var _this = this
      this.$http.get('http://127.0.0.1:8000/api/lecture/get').then(function (res) {
        console.log(res)
        var resbody = JSON.parse(response.bodyText)
        if(resbody["code"] == 0)
          _this.$message.error('查询学生失败')
        else
          _this.tableData = res.data
      })
      .catch(function (error) {
        console.log(error)
      })
    },

    // 发送请求封装的一个函数
	sendRequest(url, opt={}) {
      var _this = this
      this.$http.post(url, opt,{emulateJSON:true}).then(function (res) {
        if(url === 'http://127.0.0.1:8000/api/lecture/add') {
          console.log("添加用户信息")
          console.log(res)
          _this.tableData.push(res.data)
        } else if(url === 'http://127.0.0.1:8000/api/lecture/mod') {
          console.log("编辑用户信息")
          _this.tableData = res.data.data
        }
      })
      .catch(function (error) {
        console.log(error)
      })
    },

    sendGETRequest(url, opt={}) {
      var _this = this
      this.$http.get(url, opt).then(function (res) {
        // console.log(res)
         // 将数据存储起来
        if(url === 'http://127.0.0.1:8000/api/lecture/get') {
          // console.log("搜索用户信息")
          _this.tableData = res.data.data
        }
        else if(url === 'http://127.0.0.1:8000/api/lecture/del') {
          // console.log("删除用户信息")
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
            // 修改
              that.sendRequest('http://127.0.0.1:8000/api/lecture/mod', {params: opt})
              // this.getAllData()
           } else{
              // 新增
              that.sendRequest('http://127.0.0.1:8000/api/lecture/add', {params: that.form})
           }
              // this.getAllData()
          // that.getAllData()
          that.dialogFormVisible = false
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },

    openDialog(index) {
      this.delId = this.tableData[index]._id
      this.dialogVisible = true

    },


    delData() {
      this.sendGETRequest('http://127.0.0.1:8000/api/lecture/del',{id: this.delId})
      this.dialogVisible=false
      this.getAllData()
    },


  openDialog(index) {
    this.delId = this.tableData[index]._id
    this.dialogVisible = true

  },


  editData(index) {
      const selfData = this.tableData[index]
      this.editId = selfData._id
      this.dialogFormVisible = true
      this.isEdit = true
      this.id=selfData.id
      this.course_id=selfData.course_id
	    this.course_name=selfData.course_name
	    //this.major_name=selfData.major_name
      //this.assessment=selfData.assessment
      this.teacher_id=selfData.teacher_id
	    this.teacher_name=selfData.teacher_name
	    this.year=selfData.year
	    this.term=selfData.term
	    this.time=selfData.time
  },

  mysearch() {
      console.log('http://127.0.0.1:8000/api/lecture/get', {params: this.form})
      this.sendGETRequest('http://127.0.0.1:8000/api/lecture/get', {params: this.form})
  },
  handleOpen(key, keyPath) {
      console.log(key, keyPath);
  },

  handleClose(key, keyPath) {
    console.log(key, keyPath);
  }


	},

  watch: {
	  dialogFormVisible() {
	    if(!this.dialogFormVisible) this.isEdit=false
    },
    dialogFormSearch() {
      if(!this.dialogFormSearch) this.isSearch=false
    }
	},
  mounted: function() {
    // 组件创建时候去获取所有的用户数据
    this.getAllData();
	},
}
</script>
