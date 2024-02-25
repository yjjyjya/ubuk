<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨参考资料</span> 
    </div>
</div>

https://cn.vuejs.org/tutorial/#step-1  

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨基本语法</span> 
    </div>
</div>

### ⭕ 声明式渲染

也叫做 **响应式渲染**，能在改变时触发更新的状态被认为是响应式的  
将视图与数据进行绑定，通过改变数据的状态来自动更新视图  

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  data() {
    return {
      message: 'Hello World!',
      counter: {
        count: 0
      }
    }
  }
}).mount('#app')
</script>

<div id="app">
  <h1>{{ message }}</h1>
  <p>Count is: {{ counter.count }}</p>
</div>
```

传递给 `createApp()` 的对象是 data 组件，响应式状态被保存在其中。data 组件返回了 message 属性  
message 属性可以通过双括号法（**mustache语法**）在模板中使用，用于渲染动态文本  

> [!NOTE|style:flat]
> 双括号中可以编写 **js 代码、路径、标识符（给类、方法等起的名字）** 等  

### ⭕ 属性 Attribute 绑定

上面讲到的双括号法只能在文本中进行动态渲染  
为了给 attribute 绑定一个动态值，需要使用 `v-bind` 指令  

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  data() {
    return {
      dynamicId: 'myid',
    }
  }
}).mount('#app')
</script>

<div v-bind:id="dynamicId"></div>
或者简写
<div :id="dynamicId"></div>
```

上面给 id 赋予 dynamicId，并在 data 组件中返回 dynamicId 的值  

### ⭕ 事件监听

使用 `v-on` 指令监听 DOM 事件  

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  }
}).mount('#app')
</script>

<button v-on:click="increment">count is: {{ count }}</button>
或者简写
<button @click="increment">count is: {{ count }}</button>
```

按钮 button 绑定了 methods 选项声明的 increment 函数，用于 count 的自增  

### ⭕ 表单绑定

同时使用 `v-bind` 和 `v-on` 来在表单的输入元素上创建 **双向绑定**  

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  data() {
    return {
      text: ''
    }
  },
  methods: {
    onInput(e) {
      this.text = e.target.value
    }
  }
}).mount('#app')
</script>

<div id="app">
  <input :value="text" @input="onInput" placeholder="Type here">
  <p>{{ text }}</p>
</div>
```

> e.target.value 这个写法？？？  


### ⭕ 条件渲染

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  data() {
    return {
      awesome: true
    }
  },
  methods: {
    toggle() {
      this.awesome = !this.awesome
    }
  }
}).mount('#app')
</script>

<div id="app">
  <button @click="toggle">toggle</button>
  <h1 v-if="awesome">Vue is awesome!</h1>
  <h1 v-else>Oh no</h1>
</div>
```

上述第一个 `<h1>` 标签只会在 awesome 的值为真时进行渲染  
反之渲染第二个 `<h1>` 标签的内容，而控制 awesome 的值切换的就是 toggle 这个函数  
当然也有 `v-else-if` 的写法  

### ⭕ 列表渲染

对于一个列表要进行渲染，可以使用循环 `v-for`  

``` html
<script type="module">
import { createApp } from 'vue'

// 给每个 todo 对象一个唯一的 id
let id = 0

createApp({
  data() {
    return {
      newTodo: '',
      todos: [
        { id: id++, text: 'Learn HTML' },
        { id: id++, text: 'Learn JavaScript' },
        { id: id++, text: 'Learn Vue' }
      ]
    }
  },
  methods: {
    addTodo() {
      this.todos.push({ id: id++, text: this.newTodo })
      this.newTodo = ''
    },
    removeTodo(todo) {
      // 将不等于todo的筛选出来，即保留非todo的
      this.todos = this.todos.filter((t) => t !== todo)
    }
  }
}).mount('#app')
</script>

<div id="app">
  <form @submit.prevent="addTodo">
    <input v-model="newTodo">
    <button>Add Todo</button>    
  </form>
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      {{ todo.text }}
      <button @click="removeTodo(todo)">X</button>
    </li>
  </ul>
</div>
```

`v-for` 中的 todo 是一个局部变量，表示当前正在迭代的数组元素  
key 用于绑定每一个 todo 的唯一 id  
注意列表的 push 操作和 filter 操作  

### ⭕ 计算属性

``` html
<script type="module">
import { createApp } from 'vue'

let id = 0

createApp({
  data() {
    return {
      newTodo: '',
      hideCompleted: false,
      todos: [
        { id: id++, text: 'Learn HTML', done: true },
        { id: id++, text: 'Learn JavaScript', done: true },
        { id: id++, text: 'Learn Vue', done: false }
      ]
    }
  },
  computed: {
    // 实现计算逻辑
    filteredTodos() {
      return this.hideCompleted
        ? this.todos.filter((t) => !t.done)
        : this.todos
    }
  },
  methods: {
    addTodo() {
      this.todos.push({ id: id++, text: this.newTodo, done: false })
      this.newTodo = ''
    },
    removeTodo(todo) {
      this.todos = this.todos.filter((t) => t !== todo)
    }
  }
}).mount('#app')
</script>

<div id="app">
  <form @submit.prevent="addTodo">
    <input v-model="newTodo">
    <button>Add Todo</button>
  </form>
  <ul>
    <li v-for="todo in filteredTodos" :key="todo.id">
      <input type="checkbox" v-model="todo.done">
      <span :class="{ done: todo.done }">{{ todo.text }}</span>
      <button @click="removeTodo(todo)">X</button>
    </li>
  </ul>
  <button @click="hideCompleted = !hideCompleted">
    ｛｛ hideCompleted ? 'Show all' : 'Hide completed' ｝｝
  </button>
</div>
```

### ⭕ 生命周期和模板引用

生命周期是指 Vue 实例从创建到销毁的过程，它包含了 8 个阶段  
要手动操作 DOM，可以通过 ref attribute 来实现模板引用  

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  mounted() {
    this.$refs.pElementRef.textContent = 'mounted!'
  }
}).mount('#app')
</script>

<div id="app">
  <p ref="pElementRef">hello</p>
</div>
```

### ⭕ 侦听器

侦听器是一种可以监听数据变化的工具，它可以在数据发生变化时执行一些特定的操作  
例如当一个数字改变时将其输出到控制台  

``` html
<script type="module">
import { createApp } from 'vue'

createApp({
  data() {
    return {
      todoId: 1,
      todoData: null
    }
  },
  methods: {
    async fetchData() {
      this.todoData = null
      const res = await fetch(
        `https://jsonplaceholder.typicode.com/todos/${this.todoId}`
      )
      this.todoData = await res.json()
    }
  },
  mounted() {
    this.fetchData()
  },
  watch: {
    todoId() {
      this.fetchData()
    }
  }
}).mount('#app')
</script>

<div id="app">
  <p>Todo id: {{ todoId }}</p>
  <button @click="todoId++">Fetch next todo</button>
  <p v-if="!todoData">Loading...</p>
  <pre v-else>{{ todoData }}</pre>
</div>
```

使用 watch 选项来侦听 count 属性的变化  
当 count 改变时，侦听回调将被调用，并且接收新值作为参数  

### ⭕ 组件

``` html
<script type="module">
import { createApp } from 'vue'
import ChildComp from './ChildComp.js'

createApp({
  components: {
    ChildComp
  }
}).mount('#app')
</script>

<div id="app">
  <child-comp></child-comp>
</div>
```
``` javascript
export default {
  template: `
  <h2>A Child Component!</h2>
  `
}
```

使用 components 选项注册组件 ChildComp  
注意使用 **kebab-case** 的名字来引用  

### ⭕ 子组件接收数据

在子组件中通过 props 从父组件接受动态数据  
在父组件中可以通过 `v-bind` 传入参数，以渲染子组件的内容  

``` html
<script type="module">
import { createApp } from 'vue'
import ChildComp from './ChildComp.js'

createApp({
  components: {
    ChildComp
  },
  data() {
    return {
      greeting: 'Hello from parent'
    }
  }
}).mount('#app')
</script>

<div id="app">
  <child-comp></child-comp>
</div>
```

``` javascript
export default {
  props: {
    msg: String
  },
  template: `
  <h2>｛｛ msg || 'No props passed yet' ｝｝</h2>
  `
}
```

### ⭕ 子组件向父组件触发事件

``` html
<script type="module">
import { createApp } from 'vue'
import ChildComp from './ChildComp.js'

createApp({
  components: {
    ChildComp
  },
  data() {
    return {
      childMsg: 'No child msg yet'
    }
  }
}).mount('#app')
</script>

<div id="app">
  <child-comp @response="(msg) => childMsg = msg"></child-comp>
  <p>{{ childMsg }}</p>
</div>
```

``` javascript
export default {
  emits: ['response'],
  created() {
    this.$emit('response', 'hello from child')
    // 第一个参数是事件的名称
    // 其他所有参数都将传递给事件监听器
  },
  template: `
  <h2>Child component</h2>
  `
}
```

父组件可以使用 `v-on` 监听子组件触发的事件  
这里的处理函数接收了子组件触发事件时的额外参数，并将它赋值给了本地状态  

### ⭕ 插槽

父组件还可以通过插槽 (slot) 将模板片段传递给子组件  

``` html
<script type="module">
import { createApp } from 'vue'
import ChildComp from './ChildComp.js'

createApp({
  components: {
    ChildComp
  },
  data() {
    return {
      msg: 'from parent'
    }
  }
}).mount('#app')
</script>

<div id="app">
  <child-comp>Message: {{ msg }}</child-comp>
</div>
```

``` javascript
export default {
  template: `
  <slot>Fallback content</slot>
  `
  // <slot> 插口中的内容将被当作“默认”内容
  // 它会在父组件没有传递任何插槽内容时显示
}
```




<style>
    .note {
        background-color: #f9f9f9; 
        border: 1px solid #ddd; 
        padding: 10px; 
        border-radius: 10px; 
        display: inline-block; 
        font-weight: bold;
        margin: 10px 0px;
    }
    .note:hover {
        animation: gradient-in 0.5s forwards;
    }
    .note:not(:hover) {
        animation: gradient-out 0.5s forwards;
    }
    @keyframes gradient-in {
        0% {
            background-color: #f9f9f9;
        }
        20% {
            background-color: #f5f5f5;
        }
        100% {
            background-color: #e1e1e1;
        }
    }
    @keyframes gradient-out {
        0% {
            background-color: #e1e1e1;
        }
        80% {
            background-color: #f5f5f5;
        }
        100% {
            background-color: #f9f9f9;
        }
    }
    .title1 { 
        font-size: 24px; 
        /* color: #333;  */
    }
    .title2 { 
        font-size: 20px; 
        /* color: #555;  */
    }
    .title3 { 
        font-size: 16px; 
        /* color: #777;  */
    }
    /* .note:hover [class^="title"]{
        font-size: 30px;
        opacity: 0.6;
    } */
</style>