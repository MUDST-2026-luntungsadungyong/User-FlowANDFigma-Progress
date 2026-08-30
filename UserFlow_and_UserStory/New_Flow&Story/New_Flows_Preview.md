# Flowcharts Preview

Here are all the modified and new user flows. Since your IDE supports Mermaid rendering, you can view the flowcharts directly in this file.

## US-04 Place Order
```mermaid
flowchart TD
    subgraph Customer
        start([Start]) --> cart[View Cart]
        cart --> btnCheckout[Click 'Checkout']
        btnCheckout --> viewSummary[Review Order Summary]
        viewSummary --> btnConfirm[Click 'Confirm Order']
        viewSummary -- Cancel --> end_flow([End])
        
        btnConfirm --> viewSuccess[View Order Confirmed & Seller Contact]
        viewSuccess --> end_flow
    end
    
    subgraph System
        btnConfirm -.-> req(Request Place Order)
        req --> chkStock{Stock available?}
        chkStock -- No --> retError[Throw Error: Insufficient Stock]
        retError -.-> viewSummary
        chkStock -- Yes --> doReserve[Reserve Stock\n onHand - reserved]
        doReserve --> createOrder[Create Order\nStatus: Pending]
        createOrder -.-> viewSuccess
    end
```

## US-05 CRUD Inventory Management
```mermaid
flowchart TD
    subgraph Seller
        start([Start]) --> viewDash[Seller Dashboard]
        viewDash --> viewInv[View My Inventory]
        viewInv --> action{Choose Action}
        
        action -- Add --> viewCol[Select from Collection]
        viewCol --> fillAdd[Set Price & Stock]
        fillAdd --> submitAdd[Submit Add]
        
        action -- Edit --> fillEdit[Update Price/Stock/Info]
        fillEdit --> submitEdit[Submit Edit]
        
        action -- Delete --> confirmDel{Confirm Delete?}
        confirmDel -- Yes --> submitDel[Submit Delete]
        
        action -- Toggle Hide/Show --> submitToggle[Submit Toggle]
    end
    
    subgraph System
        submitAdd -.-> valAdd{Validate}
        valAdd -- Pass --> saveAdd[Save Product\nowner=sellerId]
        
        submitEdit -.-> valEdit{Check ownership & Validate}
        valEdit -- Pass --> saveEdit[Update Product]
        
        submitDel -.-> checkDel{In Pending Order?}
        checkDel -- Yes --> errDel[Error: Cannot Delete]
        checkDel -- No --> saveDel[Delete/Archive Product]
        
        submitToggle -.-> saveToggle[Update Visibility]
    end
```

## US-06 Seller Dashboard (Cost/Profit)
```mermaid
flowchart TD
    subgraph Seller
        start([Start]) --> viewDash[Open Seller Dashboard]
        viewDash --> inputCost[Input / Update Card Cost per item]
        inputCost --> saveCost[Save Cost]
        viewDash --> viewProfit[View Estimated Sales & Profit]
    end
    
    subgraph System
        saveCost -.-> dbCost[Update Cost in DB]
        viewProfit -.-> calc[Calculate Profit:\n(Price - Cost) * Qty]
        calc -.-> retProfit[Return Dashboard Metrics]
    end
```

## US-07 Order Management
```mermaid
flowchart TD
    subgraph Seller
        start([Start]) --> viewOrder[View 'My Sales' Orders]
        viewOrder --> selectOrder[Select a Pending Order]
        selectOrder --> action{Update Status}
        action -- Fulfilled --> btnFulfill[Mark as Fulfilled]
        action -- Cancelled --> btnCancel[Mark as Cancelled]
    end
    
    subgraph System
        btnFulfill -.-> dbFulfill[Update Order Status: Fulfilled]
        dbFulfill --> stFulfill[Reduce onHand\nReduce Reserved\nReduce Collection]
        
        btnCancel -.-> dbCancel[Update Order Status: Cancelled]
        dbCancel --> stCancel[Reduce Reserved\nRestore Available Stock]
    end
```

## US-08 User Profile (Contact)
```mermaid
flowchart TD
    subgraph Customer
        start([Start]) --> viewProfile[Go to Profile Settings]
        viewProfile --> editContact[Edit Contact Info\nPhone, Line ID, Facebook]
        editContact --> submitContact[Save Contact Info]
    end
    
    subgraph System
        submitContact -.-> valContact{Validate Form}
        valContact -- Pass --> dbContact[Update User Record]
        valContact -- Fail --> errContact[Show Error]
    end
```

## US-NEW-1 Collection Management
```mermaid
flowchart TD
    subgraph Customer_or_Seller
        start([Start]) --> viewCol[Go to My Collection]
        viewCol --> action{Choose Action}
        
        action -- Add Card --> searchCat[Search Card Catalog]
        searchCat --> fillCard[Select Condition, Foil, Lang]
        fillCard --> submitAdd[Add to Collection]
        
        action -- Edit/Delete --> modifyCol[Update details or Remove]
    end
    
    subgraph System
        submitAdd -.-> dbAdd[Save to Collection DB]
        modifyCol -.-> dbMod[Update Collection DB]
    end
```

## US-NEW-2 Seller Verification
```mermaid
flowchart TD
    subgraph Customer
        start([Start]) --> viewApply[Go to 'Become a Seller']
        viewApply --> fillForm[Fill Shop Name & Contact Info]
        fillForm --> submitForm[Submit Seller Profile]
    end
    
    subgraph System
        submitForm -.-> valForm{Validate Info}
        valForm -- Pass --> updateRole[Update sellerStatus = VERIFIED]
        updateRole -.-> retSuccess[Return Success. User can now sell.]
    end
```

## US-NEW-3 Stock Reservation Logic
```mermaid
flowchart TD
    subgraph Customer
        start([Start]) --> viewCart[View Cart]
        viewCart --> addQty[Increase Quantity]
        addQty --> submitQty[Update Cart]
    end
    
    subgraph System
        submitQty -.-> checkQty{qty <= onHand - reserved?}
        checkQty -- Yes --> updateCart[Update Cart Quantity]
        checkQty -- No --> errQty[Throw Error: Stock limit reached]
    end
```
