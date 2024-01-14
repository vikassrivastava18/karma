<template>
    <div class="row">
      <div class="col-sm">
        <h4>
          Karma
        </h4>
        <div class=" karma">
          <ul>
            <li>{{ id }}</li>
            <li>2</li>
            <li>3</li>
          </ul>
        </div>
      </div>

      <div class="col-sm">
        <h4>
          Working
        </h4>
        <div class=" doing">
          <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
          </ul>
        </div>
      </div>

      <div class="col-sm">
        <h4>
          Done
        </h4>
        <div class=" done">
          <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
          </ul>
        </div>

      </div>
    </div>
</template>

<script>
import uniqueId from "lodash.uniqueid";

export default {
  name: 'HelloWorld',
  props: {
    msg: String,
    date: String
  },
  data() {
    return {
      id: uniqueId("id-")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
