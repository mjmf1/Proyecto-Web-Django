def importe_total_carro(request):
    total = 120
    if request.user.is_authenticated:
        for key, value in request.session.get("carro", {}).items():
            total += int(value["cantidad"]) * float(value["precio"])
    return {"importe_total_carro": total}
