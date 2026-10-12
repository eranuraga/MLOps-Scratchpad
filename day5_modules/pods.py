def get_pods():
    return [
        {
            "name":"checkout",
            "status":"Running"
        },
        {
            "name":"payment",
            "status":"CrashLoopBackOff"
        }
    ]