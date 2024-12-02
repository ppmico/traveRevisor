<script>
  import { paso } from '../sharedSht.js';
  // import { canContinue } from '../sharedSht.js';
</script>
<button class = {""} onclick={()=>{paso+=1}}>
  <slot></slot>
</button>

<!-- <style>
  .disabled {
    pointer-events: none;
    color: grey;
  }
</style> -->