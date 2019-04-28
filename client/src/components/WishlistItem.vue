
<template>
    <div >
      <Wishlists v-bind:wishlists="wishlists"/>
      
        <f7-page>
          <f7-block strong>
            <br />
            <f7-row>
              <f7-col class="text-align-center">
                <f7-gauge v-bind:percent="calcPercent" v-bind:wishlists="wishlists"
                  :id="wishlist.id"
                  type="semicircle"
                  :value="percent"
                  :value-text="wishlist.name"
                  border-color="#ff9800"
                  :border-width="10"
                ></f7-gauge>
              </f7-col>
            </f7-row>
          </f7-block>
        </f7-page>
    </div>
</template>

<script>
export default {
    name: 'WishlistItem',
    props: ['wishlist'],
    data: function() {
      return {
          wishlists: [],
          
        // label: 'Attendance',
        // rate: .7378,      
      }
    },
    methods: {
      calcPercent() {
        console.log("********************************")
        percent = wishlist.goal / wishlist.added
        console.log(percent)
        return percent
      }
    },
}
</script>


<style scoped>



</style>
