// Topic: Arrays
//let prices = [7,6,4,3,1];
const prices = require('./data/ex121-stock-prices.json')

const maxProfit = (prices) => {
    // Loop thought prices and find the losses and profits from that given day to the follwing days
    // Store only profits in a empty array
    // Find the maximim in netProfitsArray
    let netProfits = []

    if(prices.length === 1){
        return 0
    } else{
        for(let i = 0; i < prices.length; i++){
            let day = i
    
            for(let x = 0; x < prices.length; x++){
                if(prices[i] !== prices[x] && day < x){
                    let net = prices[x] - prices[i]
                    netProfits.push(net)
                }
            }
    
        }
    
        let maximum = netProfits[0];
        for(let y=0; y< netProfits.length; y++){
            if(maximum < netProfits[y]){
                maximum = netProfits[y]
            } 
        }

        return Math.sign(maximum) === -1 || netProfits.length === 0 ? 0 : maximum

    }
}

maxProfit(prices)