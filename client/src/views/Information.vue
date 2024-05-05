<template>
  <div class="information">
    <div class="action">
      <div class="action-item">Extract words</div>
      <div class="action-item">Extract features</div>
      <div class="action-item">Extract all</div>
      <div class="action-item">Delete all</div>
    </div>
    <div class="information-table">
      <Table :columns="columns" :data-source="data">
        <template #headerCell="{ column }">
          <template v-if="column.key === 'name'">
            <span>
              <smile-outlined />
              Name
            </span>
          </template>
        </template>

        <template #bodyCell="{ index, column, record }">
          <template v-if="column.key === 'index'">
            <div>
              {{ index + 1 }}
            </div>
          </template>
          <template v-if="column.key === 'name'">
            <a>
              {{ record.name }}
            </a>
          </template>
          <template v-else-if="column.key === 'action'">
            <span>
              <a>Invite 一 {{ record.name }}</a>
              <a-divider type="vertical" />
              <a>Delete</a>
              <a-divider type="vertical" />
              <a class="ant-dropdown-link">
                More actions
                <down-outlined />
              </a>
            </span>
          </template>
        </template>
      </Table>
    </div>
  </div>
</template>

<script>
import { Table } from "ant-design-vue";
import axios from "axios";
export default {
  components: { Table },
  data() {
    return {
      data: [],
      columns: [
        {
          name: "Index",
          dataIndex: "index",
          key: "index",
        },
        {
          name: "Name",
          dataIndex: "name",
          key: "name",
        },
        {
          title: "Content",
          dataIndex: "content",
          key: "content",
        },
        {
          title: "Action",
          key: "action",
        },
      ],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/information/get_information_list")
      .then((res) => {
        this.data = res.data
      })
      .catch((e) => console.log(e));
  },
};
</script>

<style scoped>
.information{
    
}

.action{
    display: flex;
    justify-content: end;
}

.action-item{
    margin: 10px 20px;
    padding: 10px 20px;
    border-radius: 4px;
    background: rgb(95, 95, 192);
    color: white;
    cursor: pointer;
}
</style>