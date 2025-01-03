from app.core.domain.ports.recommendation_ports import RecommendationRepositoryPort
from app.core.domain.entities.recomendation_entity import RecommendationEntity
from tortoise import Tortoise
from typing import List


class RecommendationRepository(RecommendationRepositoryPort):
    async def get_recommendations(self) -> List[RecommendationEntity]:
        query = " WITH latest_reviews AS " \
                "(SELECT " \
                "rev_fk_loc_uuid, " \
                "rev_fk_cat_uuid, " \
                "MAX(rev_created) AS latest_rev_created " \
                "FROM review WHERE rev_created < NOW() - INTERVAL '30 days' " \
                "GROUP BY rev_fk_loc_uuid, rev_fk_cat_uuid ) " \
                "SELECT " \
                "loc.loc_uuid, " \
                "loc.loc_description, " \
                "cat.cat_uuid, " \
                "cat.cat_description, " \
                "CASE WHEN rev.rev_uuid IS NULL THEN 1 " \
                "WHEN rev.rev_created < NOW() - INTERVAL '30 days' THEN 2 ELSE 0 " \
                "END AS bandera, " \
                "rev.rev_created AS review_date " \
                "FROM " \
                "location loc " \
                "CROSS JOIN " \
                "category cat " \
                "LEFT JOIN " \
                "latest_reviews lr " \
                "ON lr.rev_fk_loc_uuid = loc.loc_uuid AND lr.rev_fk_cat_uuid = cat.cat_uuid " \
                "LEFT JOIN " \
                "review rev " \
                "ON rev.rev_fk_loc_uuid = loc.loc_uuid " \
                "AND rev.rev_fk_cat_uuid = cat.cat_uuid " \
                "AND rev.rev_created = lr.latest_rev_created " \
                "WHERE " \
                "(rev.rev_uuid IS NULL OR rev.rev_created < NOW() - INTERVAL '30 days') " \
                "ORDER BY " \
                "bandera, rev.rev_created DESC " \
                "LIMIT 10;"

        # Obtener la conexión de Tortoise
        connection = Tortoise.get_connection("default")

        # Ejecutar la consulta SQL de manera asincrónica
        result = await connection.execute_query_dict(query)

        # Mapear los resultados a objetos RecommendationEntity
        recommendations = [
            RecommendationEntity(
                loc_uuid=row[0],  # Acceder a los valores por índice
                cat_uuid=row[2],  # Acceder a los valores por índice
                bandera=row[4],  # Acceder a los valores por índice
                review_date=row[5]  # Acceder a los valores por índice
            )
            for row in result
        ]
        return recommendations
