document.addEventListener('DOMContentLoaded',()=>{
        document.querySelector('#crtOpenKey').onclick =()=>{

        let seqKey = document.querySelector('#inpSequenceKey').value;
        let m = document.querySelector('#inpKeyM').value;
        let t = document.querySelector('#inpKeyT').value;

        let open_key = function createOpenKey() {
            seqKey = seqKey.split(',');
            let i = 1;
            let n = seqKey.length;
            let open_key = [];
            seqKey.forEach(function (item, index, arr) {
                while (true) {
                    let ai = item * t % m;
                    i += 1;
                    if (i > n) {
                        open_key.push(ai);
                        break;
                    }
                }
            });
            return open_key
        };

        document.querySelector('#outOpenKey').value = open_key();
        };
});

