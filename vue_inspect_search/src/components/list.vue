<template>
  <div class="info-list">
    <el-table
      ref="listTable"
      :data="values"
      style="width: 100%">
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item label="审计日期:">
              <span>{{ props.row.date }}</span>
            </el-form-item>
            <el-form-item label="系统:">
              <span>{{ props.row.app_name }}</span>
            </el-form-item>
            <el-form-item label="系统owner:">
              <span>{{ props.row.app_owner }}</span>
            </el-form-item>
            <el-form-item label="审计内容:">
              <span>{{ props.row.content }}</span>
            </el-form-item>
            <el-form-item label="审计人员:">
              <span>{{ props.row.operator }}</span>
            </el-form-item>
            <el-form-item label="异常情况:">
              <span>{{ props.row.abnormal_result }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column
          label="审计日期"
          min-width="60">
        <template slot-scope="scope">
          <span>{{ scope.row.date  }}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="系统"
        min-width="100">
        <template slot-scope="scope">
          <span>{{ scope.row.app_name  }}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="系统owner"
        min-width="80">
        <template slot-scope="scope">
          <span>{{ scope.row.app_owner }}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="审计内容"
        min-width="220">
        <template slot-scope="scope">
          <span>{{ scope.row.content }}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="审计人员"
        min-width="80">
        <template slot-scope="scope">
          <span>{{ scope.row.operator }}</span>
        </template>
      </el-table-column>
      <el-table-column
          label="异常情况"
          min-width="300">
        <template slot-scope="scope">
          <span>{{ scope.row.abnormal_result }}</span>
        </template>
      </el-table-column>
<!--      <el-table-column label="控制" min-width="150">-->
<!--        <template slot-scope="scope">-->
<!--          <el-button-->
<!--            size="mini"-->
<!--            @click="serverEdit(scope.row)">编辑</el-button>-->
<!--          <el-button-->
<!--            size="mini"-->
<!--            type="danger"-->
<!--            @click="serverDelete(scope.row)">删除</el-button>-->
<!--        </template>-->
<!--      </el-table-column>-->
    </el-table>
  </div>
</template>

<script>

export default {
  name: 'ServerList',
  props: {
    values: {
      type: Array,
      default: function() {
        return []
      }
    },
    mulselect: {
      type: Array,
      default: function() {
        return []
      }
    }
  },
  methods: {
  }
}

</script>

<style  scoped>

  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
