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
          <el-form-item label="开课号" prop="id">
            <el-input v-model="form.id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程号" prop="course_id">
            <el-input v-model="form.course_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="老师工号" prop="teacher_id">
            <el-input v-model="form.teacher_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课日期" prop="year">
            <el-input v-model="form.year" autocomplete="off" placeholder="年"></el-input>
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
        <el-table-column label="考核方式">
          <template slot-scope="scope">
                <i v-if="scope.row.assessment===0">考试</i>
                <i v-else>当堂答辩</i>
            </template>
	      </el-table-column>
	      <el-table-column
	        prop="teacher_name"
	        label="授课老师">
	      </el-table-column>
	      <el-table-column
	        prop="year"
	        label="开课日期">
	      </el-table-column>
	      <el-table-column label="开课学期">
          <template slot-scope="scope">
                <i v-if="scope.row.term===0">春</i>
                <i v-else>秋</i>
            </template>
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
          <el-form-item label="老师工号" prop="teacher_id">
            <el-input v-model="form.teacher_id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课日期" prop="year">
            <el-input v-model="form.year" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="term">
            <el-select v-model="form.term" placeholder="请选择学期">
              <el-option style="height: 80%" label="春" value="0" autocomplete="off"></el-option>
              <el-option style="height: 80%" label="秋" value="1" autocomplete="off"></el-option>
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
	    major_name:'',
      assessment:'',
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
    addtest(){
      var _this = this
      this.$http.post(url, JSON.stringify(opt),{emulateJSON:true}).then(function (res) {
        if(url === 'http://127.0.0.1:8000/api/lecture/add') {
          console.log("添加用户信息")
          console.log(res)
          _this.tableData.push(res.data)
          _this.getAllData()
        }
      })
      .catch(function (error) {
        console.log(error)
      })

    },

    simplify(obj) {
      let newobj = new Object();
      for (let key in obj) {
        if (
          obj[key] &&
          key !== "course_name" &&
          key !== "assessment" &&
          key !== "major_name" &&
          key !== "teacher_name"
        )
          newobj[key] = obj[key];
      }
      return newobj;
    },



		// 获取所有的用户信息
    getAllData() {
      var _this = this
      this.$http.get('http://127.0.0.1:8000/api/lecture/get',{'teacher_id':JSON.parse(window.localStorage.teaInfo).id}).then(function (res) {
        console.log(res)
        var resbody = JSON.parse(res.bodyText)
        if(resbody["code"] == 0)
          _this.$message.error('开课信息失败')
        else
          _this.tableData = res.data["list"]
      })
      .catch(function (error) {
        console.log(error)
      })
    },

    // 发送请求封装的一个函数
	sendRequest(url, opt={}) {
      var _this = this
      this.$http.post(url, JSON.stringify(opt),{emulateJSON:true}).then(function (res) {
        if(url === 'http://127.0.0.1:8000/api/lecture/add') {
          console.log("添加用户信息")
          console.log(res)
          _this.tableData.push(res.data)
          _this.getAllData()
        }
        else if (url === "http://127.0.0.1:8000/api/lecture/mod") {
          console.log("编辑用户信息")
          for (let key in opt.update)
            _this.tableData[_this.editIndex][key] = opt.update[key];
          console.log(_this.tableData);
          _this.getAllData()
          }
      })
      .catch(function (error) {
        console.log(error)
      })
    },

    sendGETRequest(url, opt={}) {
      var _this = this
      this.$http.get(url, opt).then(function (res) {
        if(url === 'http://127.0.0.1:8000/api/lecture/get') {
          console.log("搜索用户信息")
          console.log(res);
          _this.tableData = res.data["list"];
        }
        else if(url === 'http://127.0.0.1:8000/api/lecture/del') {
          console.log("删除用户信息")
          console.log(_this.tableData);
          _this.tableData.splice(_this.delIndex, 1);
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
            let subForm = that.form
            delete subForm.id
            delete subForm.course_name
            delete subForm.major_name
            delete subForm.teacher_name
            let opt = {
              where: {
                id: that.editId
              },
              update: subForm
            };
            // 修改
              that.sendRequest('http://127.0.0.1:8000/api/lecture/mod', opt)
              // this.getAllData()
           } else{
              // 新增
              that.sendRequest('http://127.0.0.1:8000/api/lecture/add', that.simplify(that.form))
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



    delData() {
      this.dialogVisible=false
      this.sendGETRequest('http://127.0.0.1:8000/api/lecture/del',{params: { id: this.delId }})
      this.getAllData()
    },


  openDialog(index) {
    this.delId = this.tableData[index]["id"]
    this.delIndex = index
    this.dialogVisible = true
  },


  editData(index) {
      const selfData = this.tableData[index]
      this.editIndex = index
      this.editId = selfData.id
      this.dialogFormVisible = true
      this.isEdit = true
      this.form.id = selfData.id;
      this.form.course_id = selfData.course_id;
      this.form.teacher_id = selfData.teacher_id;
      this.form.year = selfData.year;
      this.form.term = selfData.term;
      this.form.time = selfData.time;
  },

  mysearch() {
      console.log(this.simplify(this.form))
      this.sendGETRequest('http://127.0.0.1:8000/api/lecture/get', {params: this.simplify(this.form)})
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
    this.getAllData()
	},
}
</script>
