<template>
    <div class="wrapper">
        <div class="container">
            <h2>
                KARMA {{ isAuthenticated }}
            </h2>
            <div class="cards-wrapper" id="todo">
                <card draggable="true" id="0">
                    <div class="type" style="background: #7bed9f;">
                        <img class="icon" src="https://www.svgrepo.com/show/533406/book.svg">
                        <span class="type-text">
                            Prayer
                        </span>
                    </div>
                    <span class="title">
                        Test Story
                    </span>
                    <span class="content">
                        This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
                        sed
                        diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
                    </span>
                    <div class="user-prio-wrapper">
                        <span class="user">
                            GlitchDev
                        </span>
                        <img class="icon" src="https://www.svgrepo.com/show/469842/sort-descending.svg">
                    </div>
                </card>

            </div>
        </div>

        <div class="container">
            <h2>
                SATISFIED
            </h2>
            <div class="cards-wrapper" id="done">
            </div>
        </div>

        <div class="container">
            <h2>
                UNSATISFIED
            </h2>
            <div class="cards-wrapper" id="approved">
            </div>
        </div>

    </div>
</template>


<script>
/* eslint-disable */
import CustomFetch from '@/CustomFetch';
import { mapState } from 'vuex'

export default {
    name: 'HomePage',
    computed: {
        ...mapState(['isAuthenticated']),
    },
    mounted() {
        return; 
        // self = this
        CustomFetch(`http://127.0.0.1:8080/api/token-test`, {
            method: 'GET',

            headers: {
                'Content-Type': 'application/json',
                'Authorization': localStorage.getItem(
                    'Authentication-Token'
                ),
            },
        })
            .then((data) => {
                if (data.status == 'fail') {
                    // self.$router.push({ path: '/login' });
                }
                else {
                    this.lists_data = data.slice(1)
                    this.lists = data[0]['lists']
                    console.log(this.lists)
                }

            })
            .catch((err) => {
                //   alert(err.message)
                console.log(err.message, err.status)

            })
    }
}

</script>
