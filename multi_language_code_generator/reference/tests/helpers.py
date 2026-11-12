def expected(total=0, invalid=0, visitors=0, errors=0, rate=0, size=0, paths=()):
    return dict(totalRequests=total, invalidLines=invalid, uniqueVisitors=visitors,
                errorRequests=errors, errorRateBps=rate, totalBytes=size,
                topPaths=[dict(path=p, requests=n) for p, n in paths])

