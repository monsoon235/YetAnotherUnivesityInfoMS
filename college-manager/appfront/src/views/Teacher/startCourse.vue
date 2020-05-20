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
	      </div>
		  </el-row>
      <el-collapse-transition>
        <div v-if="show1">
          <br>
          <el-form :inline="true" :model="form" :rules="searchRules" ref="form" label-width="100px" class="demo-ruleForm">
          <el-form-item label="课程号" prop="course_Id">
            <el-input v-model="form.course_Id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程名称" prop="course_name">
            <el-input v-model="form.course_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课专业" prop="course_faculty">
            <el-input v-model="form.course_faculty" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="考核方式" prop="exam_type">
            <el-input v-model="form.exam_type" autocomplete="off" placeholder="考试或当堂答辩"></el-input>
          </el-form-item>
          <el-form-item label="授课老师" prop="teacher">
            <el-input v-model="form.teacher" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课日期" prop="course_date">
            <el-input v-model="form.course_date" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="course_season">
            <el-select style='width: 100%; position: absolute; left: 138px' v-model="form.course_season" placeholder="请选择学期">
              <el-option style='height: 80%' label="春" value="春" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="秋" value="秋" autocomplete="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开课时间" prop="course_time">
            <el-input v-model="form.course_time" autocomplete="off" placeholder="周一至周五的第一到第九节"></el-input>
          </el-form-item>
        </el-form>
        <el-form-item>
          <el-button type="warning" plain @click="mysearch">搜索</el-button>
        </el-form-item>
        </div>
      </el-collapse-transition>
			<el-table
	      :data="tableData"
	      stripe
	      style="width: 100%">
	      <el-table-column
	        prop="course_Id"
	        label="课程号">
	      </el-table-column>
	      <el-table-column
	        prop="course_name"
	        label="课程名称">
	      </el-table-column>
          <el-table-column
	        prop="course_faculty"
	        label="开课专业">
	      </el-table-column>
          <el-table-column
	        prop="exam_type"
	        label="考核方式">
	      </el-table-column>
	      <el-table-column
	        prop="teacher"
	        label="授课老师">
	      </el-table-column>
	      <el-table-column
	        prop="course_date"
	        label="开课日期">
	      </el-table-column>
	      <el-table-column
	        prop="course_season"
	        label="开课学期">
	      </el-table-column>
	      <el-table-column
	        prop="course_time"
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
          <el-form-item label="课程号" prop="course_Id">
            <el-input v-model="form.course_Id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程名称" prop="course_name">
            <el-input v-model="form.course_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课专业" prop="course_faculty">
            <el-input v-model="form.course_faculty" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="考核方式" prop="exam_type">
            <el-input v-model="form.exam_type" autocomplete="off" placeholder="考试或当堂答辩"></el-input>
          </el-form-item>
          <el-form-item label="授课老师" prop="teacher">
            <el-input v-model="form.teacher" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课日期" prop="course_date">
            <el-input v-model="form.course_date" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="course_season">
            <el-select style='width: 100%; position: absolute; left: 138px' v-model="form.course_season" placeholder="请选择学期">
              <el-option style='height: 80%' label="春" value="春" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="秋" value="秋" autocomplete="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开课时间" prop="course_time">
            <el-input v-model="form.course_time" autocomplete="off" placeholder="周一至周五的第一到第九节"></el-input>
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
      course_Id:'',
	    course_name:'',
	    course_faculty:'',
	    exam_type:'',
	    teacher:'',
	    course_date:'',
	    course_season:'',
	    course_time:''
      },
      rules: {
        course_date: [
          { type: 'number', message: '日期必须是数字', trigger: 'blur'}
        ]
      },
      searchRules: {

      },
  }},
methods: {
		// 获取所有的用户信息
    getAllData() {
      var _this = this
      this.$http.get('http://127.0.0.1:8000/api/course/get').then(function (res) {
        console.log(res)
        var resbody = JSON.parse(response.bodyText)
        if(resbody["code"] == 1)
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
      this.$http.get(url, opt).then(function (res) {
        // console.log(res)
         // 将数据存储起来
        if(url === 'http://127.0.0.1:8000/api/course/add') {
          // console.log("添加用户信息")
          // console.log(res)
          _this.tableData.push(res.data)
        } else if(url === 'http://127.0.0.1:8000/api/course/mod') {
          // console.log("编辑用户信息")
          _this.tableData = res.data.data
        }
        else if(url === 'http://127.0.0.1:8000/api/course/get') {
          // console.log("搜索用户信息")
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
              that.sendRequest('http://127.0.0.1:8000/api/teacher/mod', {params: opt})
              // this.getAllData()
           } else{
              // 新增
              that.sendRequest('http://127.0.0.1:8000/api/teacher/add', {params: that.form})
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


  editData(index) {
      const selfData = this.tableData[index]
      this.editId = selfData._id
      this.dialogFormVisible = true
      this.isEdit = true
      this.course_Id=selfData.course_Id
	    this.course_name=selfData.course_name
	    this.course_faculty=selfData.course_faculty
	    this.exam_type=selfData.exam_type
	    this.teacher=selfData.teacher
	    this.course_date=selfData.course_date
	    this.course_season=selfData.course_season
	    this.course_time=selfData.course_time
  },

  mysearch() {
      console.log('http://127.0.0.1:8000/api/course/get', {params: this.form})
      this.sendRequest('http://127.0.0.1:8000/api/course/get', {params: this.form})
    },


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