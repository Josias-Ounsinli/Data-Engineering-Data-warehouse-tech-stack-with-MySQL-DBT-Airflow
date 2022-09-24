source as (
    select *
    from source('first_transformation', 'cars')
),

final as(
    select track_id::string as track_id
        traveled_d as traveled_d
        avg_speed as avg_speed
    from source
)

select *
from final