from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/kmeans",
                   tags=["kmeans"],
                   responses={status.HTTP_404_NOT_FOUND:{"message": "No encontrado"}})


@router.post('/entrenamiento')
async def entrenamiento():
    return {'kmeans':'entrenamiento'}                   