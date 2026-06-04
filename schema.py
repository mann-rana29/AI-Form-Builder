from pydantic import BaseModel, Field
from typing import Optional, Any


class PropsSchema(BaseModel):
    label: str
    required: bool = False
    hidden: bool = False

    placeholder: Optional[str] = None

    short_label: Optional[str] = Field(
        default=None,
        alias="shortLabel"
    )

    query_key: Optional[str] = Field(
        default=None,
        alias="queryKey"
    )

    width: Optional[int] = 100

    min_length: Optional[int] = Field(
        default=None,
        alias="minLength"
    )

    max_length: Optional[int] = Field(
        default=None,
        alias="maxLength"
    )

    auto_complete: Optional[str] = Field(
        default=None,
        alias="autoComplete"
    )

    class Config:
        populate_by_name = True


class ElementSchema(BaseModel):
    id: str

    element_type: str = Field(
        alias="elementType"
    )

    props: PropsSchema

    class Config:
        populate_by_name = True


class ImageSchema(BaseModel):
    file: Optional[Any] = None
    url: str = ""


class UiStateSchema(BaseModel):

    is_previewing: bool = Field(
        default=False,
        alias="isPreviewing"
    )

    canvas_view: str = Field(
        default="desktop",
        alias="canvasView"
    )

    canvas_columns: int = Field(
        default=1,
        alias="canvasColumns"
    )

    field_spacing: int = Field(
        default=16,
        alias="fieldSpacing"
    )

    label_alignment: str = Field(
        default="left",
        alias="labelAlignment"
    )

    show_label: bool = Field(
        default=True,
        alias="showLabel"
    )

    input_style: str = Field(
        default="box",
        alias="inputStyle"
    )

    form_width: int = Field(
        default=650,
        alias="formWidth"
    )

    label_width: int = Field(
        default=100,
        alias="labelWidth"
    )

    padding_top: int = Field(
        default=40,
        alias="paddingTop"
    )

    padding_right: int = Field(
        default=40,
        alias="paddingRight"
    )

    padding_bottom: int = Field(
        default=30,
        alias="paddingBottom"
    )

    padding_left: int = Field(
        default=40,
        alias="paddingLeft"
    )

    background_color: str = Field(
        default="#ffffff",
        alias="backgroundColor"
    )

    font_color: str = Field(
        default="#000000",
        alias="fontColor"
    )

    input_background_color: str = Field(
        default="#FFFFFF",
        alias="inputBackgroundColor"
    )

    background_image: ImageSchema = Field(
        default_factory=ImageSchema,
        alias="backgroundImage"
    )

    header_image: ImageSchema = Field(
        default_factory=ImageSchema,
        alias="headerImage"
    )

    border_width: int = Field(
        default=1,
        alias="borderWidth"
    )

    corner_radius: int = Field(
        default=4,
        alias="cornerRadius"
    )

    border_color: str = Field(
        default="#D3D3D3",
        alias="borderColor"
    )

    border_style: str = Field(
        default="solid",
        alias="borderStyle"
    )

    shadow_color: str = Field(
        default="#00000020",
        alias="shadowColor"
    )

    shadow_horizontal: int = Field(
        default=0,
        alias="shadowHorizontal"
    )

    shadow_vertical: int = Field(
        default=2,
        alias="shadowVertical"
    )

    shadow_blur: int = Field(
        default=8,
        alias="shadowBlur"
    )

    shadow_spread: int = Field(
        default=0,
        alias="shadowSpread"
    )

    input_font_color: str = Field(
        default="#000000",
        alias="inputFontColor"
    )

    active_tag_color: str = Field(
        default="#2563EB",
        alias="activeTagColor"
    )

    input_border_width: int = Field(
        default=1,
        alias="inputBorderWidth"
    )

    input_border_color: str = Field(
        default="#D3D3D3",
        alias="inputBorderColor"
    )

    input_corner_radius: int = Field(
        default=10,
        alias="inputCornerRadius"
    )

    input_width: str = Field(
        default="100%",
        alias="inputWidth"
    )

    input_border_style: str = Field(
        default="solid",
        alias="inputBorderStyle"
    )

    input_padding_top: int = Field(
        default=12,
        alias="inputPaddingTop"
    )

    input_padding_right: int = Field(
        default=12,
        alias="inputPaddingRight"
    )

    input_padding_bottom: int = Field(
        default=12,
        alias="inputPaddingBottom"
    )

    input_padding_left: int = Field(
        default=12,
        alias="inputPaddingLeft"
    )

    input_shadow_color: str = Field(
        default="#00000010",
        alias="inputShadowColor"
    )

    input_shadow_horizontal: int = Field(
        default=0,
        alias="inputShadowHorizontal"
    )

    input_shadow_vertical: int = Field(
        default=1,
        alias="inputShadowVertical"
    )

    input_shadow_blur: int = Field(
        default=4,
        alias="inputShadowBlur"
    )

    input_shadow_spread: int = Field(
        default=0,
        alias="inputShadowSpread"
    )

    label_color: str = Field(
        default="#000000",
        alias="labelColor"
    )

    label_font_family: str = Field(
        default="Open Sans",
        alias="labelFontFamily"
    )

    label_font_size: int = Field(
        default=14,
        alias="labelFontSize"
    )

    label_font_weight: int = Field(
        default=400,
        alias="labelFontWeight"
    )

    short_label_color: str = Field(
        default="#666666",
        alias="shortLabelColor"
    )

    short_label_font_family: str = Field(
        default="Open Sans",
        alias="shortLabelFontFamily"
    )

    short_label_font_size: int = Field(
        default=12,
        alias="shortLabelFontSize"
    )

    short_label_font_weight: int = Field(
        default=400,
        alias="shortLabelFontWeight"
    )

    placeholder_color: str = Field(
        default="#74797B",
        alias="placeholderColor"
    )

    placeholder_font_family: str = Field(
        default="Noto Sans JP",
        alias="placeholderFontFamily"
    )

    placeholder_font_size: int = Field(
        default=14,
        alias="placeholderFontSize"
    )

    placeholder_font_weight: int = Field(
        default=400,
        alias="placeholderFontWeight"
    )

    class Config:
        populate_by_name = True